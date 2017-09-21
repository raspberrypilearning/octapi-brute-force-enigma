## Crypt attack on Enigma messages with Raspberry Pi

In this next section, we will develop a brute force crypt attack on the Enigma cipher text, which means we will simply exhaust search over all possible machine settings to try and find which one was used. For the time being, we will ignore the plug board setting (and assume that is known).

We will use a crib text with our cipher text, which is a guess at what the cipher text might be. This may seem like a cheat, but is actually exploiting a weakness of the Enigma system as used during WWII: some of the text in messages was predictable, especially at the start.

    ciphertext = "YJPYITREDSYUPIU"
    cribtext = "THISXISXWORKING"

We need to represent the selection of three out of five rotor wheels in our Python code. We could write code to generate the possibilities, but as there aren't very many, we can manually define them.

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

We will now select a choice of rotors from the above list and pass them to a function that tries to decrpyt the cipher text to obtain the crib text. Let's write a 'find_rotor_start()' function so that it returns the rotor choice and the rotor start position that worked. We will return "null" for all rotor combinations that didn't work.

Here's how we will use it with our list of rotor orders.

    for rotor_setting in rotor:
        rotor_choice, start_pos = find_rotor_start( rotor_setting, ciphertext, cribtext )

Most of the time our function will fail to match the cipher and crib text because the rotor choice will be wrong. On one occasion (hopefully) the cipher and crib texts will match because we have found the machine setting used.

Inside our function we will need to search over all possible rotor start positions. We are not yet searching over rotor slip ring settings, so we can do this with three nested loops.


    def find_rotor_start( rotor_choice, ciphertext, cribtext ):

        from enigma.machine import EnigmaMachine

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        machine = EnigmaMachine.from_key_sheet(
           rotors=rotor_choice,
           reflector='B',
           ring_settings='1 1 1',					# no ring setting
           plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')		# plugboard known

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


We have imported the Py-enigma module inside our function for a reason: this allows us to use this code later on in an OctaPi cluster so that we can run the search massively in parallel in much shorter time than we can on a single processor. For the time being, we will run our code on a standalone Raspberry Pi.

### Coding challenge
Create a valid cipher text using procedure shown earlier in this resource. You can either run pyenigma.py with the correct parameters to do this or write Python code to do it like the test code we had at the start of this resource if you are running in an environment that does not support command line parameters. For the time being use "1 1 1" for the ring settings to simplify your code. Now assemble the segments of Python code above into a program that searches over all possible rotor settings to find the settings you used. You can hard code the plug board settings into your 'find_rotor_start()' function code to match what you used to encrypt the message. Make sure these match.

Our code for doing this is available [here](source\enigma_bf_standalone.py).

### Question
We did not code the rotor slip ring settings. This setting allows the letters on each of the rotors to be shifted round (A to B, A to C, A to D, etc...). To deal with the rotor ring setting, we will need to modify and run the 'find_rotor_start()' function repeatedly for every rotor slip ring setting.

How much longer will it take to run our program if we code for a search over slip ring settings as well?

### Answer
If we have an Enigma machine with three rotors, each rotor can have 26 slip ring positions (A to A (no shift), A to B, ..., A to Z, etc...). That means we have to run the search for the start position 26 times for the first rotor, and all of that 26 times for the second rotor, and all of that 26 times for the third rotor. So our brute force crypt attack program will take 26 x 26 x 26 = 17,576 times longer.

This is a very long time, but we could break up the problem into many parts and run thse in parallel using OctaPi. This is what we will do next.
