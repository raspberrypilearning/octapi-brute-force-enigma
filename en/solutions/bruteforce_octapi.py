import dispy, socket

ciphertext = input('Cipher text ')
cribtext = input('Crib text ')
ring_choice = input('Ring settings ')

rotors = [ "I II III", "I II IV", "I II V", "I III II",
"I III IV", "I III V", "I IV II", "I IV III",
"I IV V", "I V II", "I V III", "I V IV",
"II I III", "II I IV", "II I V", "II III I",
"II III IV", "II III V", "II IV I", "II IV III",
"II IV V", "II V I", "II V III", "II V IV",
"III I II", "III I IV", "III I V", "III II I",
"III II IV", "III II V", "III IV I", "III IV II",
"III IV V", "IV I II", "IV I III", "IV I V",
"IV II I", "IV II III", "IV I V", "IV II I",
"IV II III", "IV II V", "IV III I", "IV III II",
"IV III V", "IV V I", "IV V II", "IV V III",
"V I II", "V I III", "V I IV", "V II I",
"V II III", "V II IV", "V III I", "V III II",
"V III IV", "V IV I", "V IV II", "V IV III" ]


def find_rotor_start( rotor_choice, ciphertext, cribtext, ring_choice ):
    from enigma.machine import EnigmaMachine
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    machine = EnigmaMachine.from_key_sheet(
       rotors=rotor_choice,
       reflector='B',
       ring_settings=ring_choice,		
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')		

    # Do a search over all possible rotor starting positions
    for rotor1 in alphabet:          # Search for rotor 1 start position
        for rotor2 in alphabet:      # Search for rotor 2 start position
            for rotor3 in alphabet:  # Search for rotor 3 start position

                # Generate a possible rotor start position
                start_pos = rotor1 + rotor2 + rotor3

                # Set the starting position
                machine.set_display(start_pos)

                # Attempt to decrypt the plaintext
                plaintext = machine.process_text(ciphertext)
                print( plaintext )

                # Check if decrypted version is the same as the crib text
                if plaintext == cribtext:
                    print("Valid settings found!")
                    return rotor_choice, ring_choice, start_pos

    # If we didn't manage to successfully decrypt the message
    return rotor_choice, ring_choice, "Cannot find settings"


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80)) # doesn't matter if 8.8.8.8 can't be reached
cluster = dispy.JobCluster(find_rotor_start, ip_addr=s.getsockname()[0], nodes='192.168.1.*')

jobs = []
id = 1

for rotor_choice in rotors:
    job = cluster.submit( rotor_choice, ciphertext, cribtext, ring_choice )
    job.id = id # Associate an ID to the job
    jobs.append(job)
    id += 1   # Next job
    print( "Waiting..." )
    cluster.wait()
    print( "Collecting job results" )

found = False
for job in jobs:
    # Wait for job to finish and return results
    rotor_setting, ring_setting, start_pos = job()

    # If a start position was found
    if start_pos != "Cannot find settings":
        found = True
        print( "Rotors %s, ring %s, message key was %s, using crib %s" % (rotor_setting, ring_setting, start_pos, cribtext) )

if found == False:
    print( 'Attack unsuccessful' )

cluster.print_status()
cluster.close()
