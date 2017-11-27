# This code attempts a partial brute force attack on Enigma messages.
# Messages may be created on a real machine, compatible replica, the 
# Cryptoy Android App or any application that accurately reproduces
# the 3-rotor machine used by the german armed forces. We have used 
# Brian Neal's Py-enigma Python3 library and utilities. 
#
# This code runs standalone on the client and allows you to compare 
# compute runtime with the Dispy version running on OctaPi. 
#

# Dispy:
# Giridhar Pemmasani, "dispy: Distributed and parallel Computing with/for Python",
# http://dispy.sourceforge.net, 2016

# Py-enigma:
# Brian Neal
# http://py-enigmareadthedocs.org/
# License: MIT License

# All other original code: Crown Copyright 2016, 2017 

# Assumes message was encrypted as follows:
#
# STEP 1: Choose a start position and message key
# where: 	UYT is initial rotor position (chosen 'randomly')
#		SCC is unencrypted message key (chosen 'randomly')
#	
# STEP 2: Encrypyt the message key
#	pyenigma.py -r II V III -i 1 1 1 -p AV BS CG DL FU HZ IN KM OW RX -u B --start=UYT --text='SCC'
#	PWE
# where: 	PWE is encrypted message key
#
# Note: We use a one-to-one relation for the rotor ring for compatability with Cryptoy 
#
# STEP 3: Encrypt the message using the unencrypted message key 
#	pyenigma.py --key-file=keys.txt --start='SCC' --text='THISXISXWORKING'
#	YJPYITREDSYUPIU
# where:
#	SCC is the unencrypted message key
#	YJPYITREDSYUPIU is the cypher text produced
#	
# STEP 4: Operator sends (usually in Morse):
#	STNA DE STNB 1104 = 15 = UYT PWE = BNUGZ YJPYI TREDS YUPIU
# where:
#	STNA is callsign of destination station
#	DE means 'from' in Morse abreviation
#	STNB is callsign of originating station
#	= is the 'break' Morse character, which is used as a delimiter
#	1104 is time message is sent (presumably UTC)
# 	BNUGZ contains UGZ 'Kenngruppen' (day indicator for confirmation of correct key sheet entry on decrypt)
#
#

################################
# Brute Force attack
# This is a limited brue force attack on the rotor settings assuming no plugboard and no rotor ring
# We use 'THISXISXWORKING' as the crib message
################################

rotor = [ 	"I II III", 	"I II IV", 	"I II V",  	"I III II", 
		"I III IV", 	"I III V", 	"I IV II", 	"I IV III", 
		"I IV V", 	"I V II", 	"I V III", 	"I V IV",
		"II I III", 	"II I IV", 	"II I V", 	"II III I", 
		"II III IV", 	"II III V", 	"II IV I", 	"II IV III", 
		"II IV V", 	"II V I", 	"II V III", 	"II V IV",
		"III I II",	"III I IV",	"III I V",	"III II I",
		"III II IV", 	"III II V",	"III IV I",	"III IV II",
		"III IV V", 	"IV I II",	"IV I III",	"IV I V",
		"IV II I",	"IV II III",	"IV I V",	"IV II I",
		"IV II III",	"IV II V",	"IV III I",	"IV III II",
		"IV III V",	"IV V I",	"IV V II",	"IV V III",
		"V I II",	"V I III",	"V I IV",	"V II I",
		"V II III", 	"V II IV",	"V III I",	"V III II",
		"V III IV",	"V IV I",	"V IV II",	"V IV III"	]

#
# This function does an exhaust search over the list of possible
# rotor selections
#
def find_rotor_start( rotor_choice, ciphertext, cribtext ):

    from enigma.machine import EnigmaMachine

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    machine = EnigmaMachine.from_key_sheet(
       rotors=rotor_choice,
       reflector='B',
       ring_settings='1 1 1',					# no ring setting
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')	# plugboard known


    # do an exhaust search over all possible rotor starting positions
    for i in range(len(alphabet)):            # search for rotor 1 start position
        for j in range(len(alphabet)):        # search for rotor 2 start position
            for k in range(len(alphabet)):    # search for rotor 3 start position
                # generate a possible rotor start position
                start_pos = alphabet[i] + alphabet[j] + alphabet[k]

                # set machine initial starting position and attempt decrypt
                machine.set_display(start_pos)
                plaintext = machine.process_text(ciphertext)

                # check if decrypt is the same as the crib text
                if (plaintext == cribtext):
                    # print( start_pos, plaintext, cribtext )
                    return( rotor_choice, start_pos )

    return( rotor_choice, "null" )


# main loop
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("ciphertext", help="cipher text, which is the encrypted text to be broken")
    parser.add_argument("cribtext", help="crib text, which is known message content")
    args = parser.parse_args()

    # extract the cipher and crib texts from the command line
    ciphertext = args.ciphertext
    cribtext = args.cribtext

    print(( "Brute force crypt attack on Enigma message %s using crib %s" % (ciphertext, cribtext) ))

    # try all rotor settings (choosing three from five)
    for rotor_setting in rotor:
        print(( "Trying rotors %s..." % (rotor_setting) ))
        rotor_choice, start_pos = find_rotor_start( rotor_setting, ciphertext, cribtext )
        if (start_pos != "null"):
            print(( "Machine setting found: rotors %s, message key was %s, using crib %s" % (rotor_choice, start_pos, cribtext) ))
            exit(0) 
