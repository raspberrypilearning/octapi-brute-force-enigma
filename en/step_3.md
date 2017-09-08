## Brute Force Crypt Attack on Enigma

## Check py-enigma
To check that the software has installed properly, let's try writing some simple Python 3 test code and using it to decrpyt this message: "YJPYITREDSYUPIU". Don't worry too much about what all the steps are for at this stage, we'll look in more detail at this later. For now, let's create a new Python 3 script and code each step of the process as follows.

First, we need to import the EnigmaMachine module from Py-enigma.

    from enigma.machine import EnigmaMachine

Next, we setup an Enigma machine object. We'll need to match the settings that were used with the machine that encrpyted the message. The code looks like this.

    machine = EnigmaMachine.from_key_sheet(
       rotors='II V III',
       reflector='B',
       ring_settings='1 1 1',
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

Now, we set the initial position of the Enigma machine rotors to U, Y and T. This also matches the sending machine.

    machine.set_display('UYT')

We were sent "PWE" as the encrypted key for this message. It was encrypted before sending to prevent an eavesdropper from being able to read it. However, our Enigma machine can recover the actual message key used by decrypting "PWE" using the rotor start position we just set: U, Y and T. We then reset the Enigma machine's rotor starting positions with the decrypted message key.

    msg_key = machine.process_text('PWE')
    machine.set_display(msg_key)

We are now ready to decrypt the message. If the message text we received was "YJPYITREDSYUPIU", we can decrypt it using the following:

    ciphertext = 'YJPYITREDSYUPIU'
    plaintext = machine.process_text(ciphertext)

    print(plaintext)

If all is well, you should see the Python 3 script exit without error with "THISXISWORKING".

## What is Enigma and how did it work?

Enigma was a cypher machine created in the early 20th century for commercial, diplomatic and military applications. The machine was adopted by the German military during World War II for secret communications. The Enigma encryption code was famously broken at Bletchley Park, the forerunner of GCHQ, during WWII and intercepted radio messages from the German military successfully read. This spectacular acheievement is thought to have shortened the war, and saved many lives on both sides of the conflict.

From an electrical point of view, the Enigma machine is simply a battery, bulb and switch circuit. There is no electronics, it it an electro-mechanical device. The encryption was achieved by varying the path of an electric current through the wiring of the machine. A number of rotors having 26 contacts, one for each of the letters A-Z, were stack0ed together to create the current path though the heart of the machine. There were electrical contacts on both sides of each rotor wheel and a jumble of wiring between them so that the letters were transposed from one side to the other. By stacking several rotors and using a reflector at the end to return the current back through the rotors, it was possible to achieve many transpositions per letter, making it almost impossible to read the text. As if this wasn't enough, a plug board was added to the original design which allowed up to ten pairs of letters to be manually transposed as they went into the rotors and again when they came back out.

  ![Encoding a W as G on Enigma](images/Enigma-wiring.gif)

In the diagram above, we show how a character on the keyboard went through many stages of transposition before being routed to a lightbulb on the lampboard represented the encrypted letter. The user would type their plain text message character by character on the keyboard and read the cypher text as each bulb was illuminated on the lampboard in response.

The Enigma machine had several complications. First, three rotors were selected from five that were available (there were also machines that used four rotors). The bottommost rotor advanced as the message was typed so that a different transposition of letters was used character by character. After the first rotor had advanced 26 positions, it advanced the next rotor by one, and so on. It was also possible to slip round the letter assignments on the side of the rotor wheel so that A = B, or A = C, etc. This made the encryption sequence discontinuous by changing the point at which the rotors advanced.

Combining three rotors from a set of five, the rotor settings with 26 positions, and the plugboard with ten pairs of letters connected, the military Enigma has 158,962,555,217,826,360,000 (nearly 159 quintillion) different settings.

  ![Close-up view of rotor from a WWII captured Enigma machine](images/7X5A0921-closeup.png)

In the photo above, we can see the jumble of wiring inside an expanded rotor wheel from a WWII captured Enigma machine.

The encryption relied on both the sending and receiving Enigma machines being set the same. To do this, a settings sheet was used at both communicating stations. The sheet specified:
- which rotors (of those available) should be selected and what order they should be inserted into the machine
- how much each rotor should be slipped round
- what letters should be changed by the plug board
- what rotor start position should be used

A different set of machine settings was used each day, and the rotor start position was changed every six hours, so the machine setting was very time sensitive. The user also selected three characters for themselves as a one-off message key for each message sent.

  ![A captured Enigma settings sheet held by GCHQ](images/Enigma-settings-sheet.jpg)

This is an Enigma settings sheet captured at the end of WWII which has been released by GCHQ for this project. You can see how the various settings are laid out in the expanded view of one of the lines on the sheet shown below.  

  ![A line of settings from a WWII captured Enigma settings sheet](images/Enigma-settings-line.jpg)

The settings we've highlighted are for the first day of the month and show that rotors IV, I and V should be selected and used in that order. The ring settings follow: rotor IV should be slipped round to position 20 (A = T), rotor I to 5 (A = E) and rotor V to position 10 (A = J). Next the wiring of the plug board should be S to X, K to U, Q to F, etc... Finally, the start position for the rotors should be "SRC", "EEJ, "FNZ" and "SZK" for each 6-hour period of the day.

There were two reflectors used, B or C. These had fixed transpositions of letters which ensured that the current returned back through the machine without it reversing the transposition on the return leg. We will assume reflector B has been used.

Lets use the Py-enigma command line tool to create a message using the settings from the sheet.

- Rotors in use (and order placed in machine): IV I V
- Rotor slip ring settings: 20, 5, 10
- Plug board: SX KU QP VN JG TC LA WM OB ZF
- Reflector: B
- Rotor start position: FNZ

If your message is "RASPBERRYPI", you need to run Py-enigma as follows.

    pyenigma.py -r IV I V -i 20 5 10 -p SX KU QP VN JG TC LA WM OB ZF -u B -s FNZ -t "RASPBERRYPI"

This should return with, "NHBEEFAMZCJ", as the encrypted text.

Our test code is [here](source/enigma_test.py)

Try other settings from the sheet to see how the text changes.

### Question
Do any of the characters get encrypted as themselves (ie does "A" get encrypted as "A", "B" as "B", etc...)

### Answer
No. In fact this is a weakness of the Enigma system because an attacker can eliminate all possible crypt attack solutions where an "A" is decrypted as an "A", and so on.

## Enigma in use during WWII

Enigma messages were normally sent in Morse code over shortwave radio. This means they could easily be intercepted some distance away, so there was heavy reliance on the strength of the encryption technique to keep the messages secret. In the event, it was possible for the messages to be received in Britain and successfully decrypted at Bletchley Park.

Let's have a look at how messages were sent so that we can create a message authentically using Py-enigma then develop Python code to crypt attack it.

A number of different radio procedures were used by the different parts of the German military, but they all looked a bit like this (we assume the machines have been set the same from the machine setting sheet). This is what we would have received if we were intercepting an Enigma encrypted transmission.

### STEP 1: Select the rotors and choose a three character message key
We find the line on the settings sheet that corresponds to the current day of the month. Which rotors to use and in what order is the first thing on the settings sheet. The rotor start position for the current 6 hour period is on the end of the line. The message key, which should be unique to every message, could not be sent in the clear (for fairly obvious reasons), so it was encrypted for transmission.

Example:
Assume the settings sheet tells us to select rotors, II, V and III and insert them into the machine left to right with the starting positions to U, Y and T. We think of SCC as our message key (choosing it at random).

### STEP 2: Encrypyt the message key
When we type "SCC" on the Enigma keyboard, we obtain "PWE" as the encrypted form of the message key. This is safe to send over a radio channel.

In Py-enigma, we can reproduce this as follows.

    pyenigma.py -r II V III -i 1 1 1 -p AV BS CG DL FU HZ IN KM OW RX -u B --start=UYT --text='SCC'

For at least part of WWII, the German military procedure was to send the message key encrypting it twice, in our example they would have typed "SCCSCC" and obtained "PWEHVF".

### Question
There is a flaw with repeating the message key, what is it?

### Answer
We previous found that no plain text letters get encrypted as themselves. This means that we know that the message key cannot possibly be "P" for the first letter, "W" for the second, or "E" for the third. In addition if the message key is sent twice, we also know it cannot be "H", followed by "V" followed by "F". This reduces the amount of searching required to find the plain text letters because the first letter is neither "P" or "H", and so on.

### STEP 3: Encrypt our message using the unencrypted message key
Once the message key was chosen and encrypted, the machine was reset to the unencrypted version of the key and the message was typed into the keyboard. Numbers had to be spelled out in full (because there were no number keys), also a space was often indicated by the letter 'X' because there was no space bar.

So if we wanted to say "this is working", we would type "THISXISXWORKING"

In Py-enigma, this look like:

    pyenigma.py -r II V III -i 1 1 1 -p AV BS CG DL FU HZ IN KM OW RX -u B --start='SCC' --text='THISXISXWORKING'

YJPYITREDSYUPIU is the cypher text produced assuming SCC is the unencrypted message key.

### STEP 4: Radio operator sends the encrypted message and everything needed for secret decryption (in Morse code)
The radio operator would have sent the message in Morse code using a series of callsigns and abreviated text (like texting abreviations are used on a on a mobile phone reduce the amount of typing needed).

### To read more
If you want to know more about the story of breaking the Enigma code, the following book will be of interest: "Dilly - The Man Who Broke Enigmas", Mavis Batey, ISBN 9781906447151, Biteback.

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

## Crypt attack on Enigma messages using OctaPi

### Installing Py-enigma on OctaPi
Before you begin, you will need to install  [Py-enigma by Brian Neal](http://py-enigmareadthedocs.org/) on both your client machine and all the servers in your OctaPi cluster.

Start with the client machine

1. Boot up the client and connected to the Internet. This will mean disconnecting from your OctaPi router and connecting to your Wi-Fi for Internet access.

1. Once on-line, open a terminal window

    ![Open a terminal](images/terminal.png)

1. To install Brian Neal's Py-enigma on the OctaPi client, run the following commands.

    sudo pip3 install py-enigma
    sudo pip3 --upgrade py-enigma

This sequence of commands installs a Python 3 module and also a pyenigma.py command line Python application ready to use.

1. Disconnect the OctaPi client from the Internet and re-connect to your OctaPi Wi-Fi network

1. We need to remove any previous Wi-Fi information to avoid confusion.

    In a terminal window, type the following command to edit the `wpa_suplicant.conf` file:

    ```bash
    sudo nano \etc\wpa_suplicant\wpa_suplicant.conf
    ```

    Remove any entries in `wpa_suplicant` that are for Wi-Fi networks other than OctaPi, then press `Ctrl` + `o` to save and `Ctrl` + `x` to exit.

    **Important:** If alternative Wi-Fi networks are not removed, your client may log onto the wrong network.

Next, do the same for each of the servers.

1. Select one server, then connect and keyboard screen and mouse to it so that you can administer it directly from a terminal winow

1. Repeat all the steps needed to install Py-enigma that you followed for the client.

1. Remember to remove any entries in `wpa_suplicant` that are for Wi-Fi networks other than OctaPi

1. Shutdown the server and either repeat the installation the same way for the rest of the servers in you cluster, or replicate the microSD card.

## Running Py-enigma on OctaPi

To do an exhaust search of all rotor slip ring settings, we will need to run a lot of jobs on OctaPi using [Dispy](http://dispy.sourceforge.net/index.html). The demand on the OctaPi client machine for memory will be quite large, so we will need to run the program one ring setting at a time (if we are using the simple 'canonical' form of the code).

The OctaPi code using Dispy is very similar to the code we created for a standalone processor.

We will run the program using command line arguments in order to set the cipher text, crib text and rotor slip ring settings at run time. If our Python code is called 'enigma_bf_canonical.py', the command line will look like:

    sudo python3 enigma_bf_canonical.py 'FKFPQZYVON' 'CHELTENHAM' '1 1 1'

 Where
     'FKFQQZYVON' is cipher text produced by an Enigma machine, or the pyenigma.py utility
     'CHELTENHAM' is text that was encrrypted, we are using it as a crib

Starting with the code we wrote for a standalone processor, we need to create a cluster object on our OctaPi network and fill it with 'find_rotor_start()' jobs. This code goes in the main loop in the 'enigma_bf_canonical.py' script.

        cluster = dispy.JobCluster(find_rotor_start, nodes='192.168.1.*')
        jobs = []
        id = 1    # job id

        # submit the jobs for this ring choice
        for rotor_choice in rotor:
            job = cluster.submit( rotor_choice, ring_choice, ciphertext, cribtext )
            job.id = id # associate an ID to the job
            jobs.append(job)
            id += 1   # next job

In this code snippet we create the cluster object, then create a job for each call of 'find_rotor_start()'. The parameters are passed in the 'cluster.submit()' function call. The 'rotor' array is the same as we had before.

Next we need to wait for the jobs to complete before collecting the results returned from the cluster.

        print( "Waiting..." )
        cluster.wait()
        print( "Collecting job results" )

The last step is to sift through the results to see if any of the find_rotor_start() jobs didn't return the string "null", in which case the returned string must havce been a valid rotor start position (three characters).

        # collect and check through the jobs for this ring setting
        found = False
        for job in jobs:
            rotor_setting, ring_setting, start_pos = job() # waits for job to finish and returns results
            if (start_pos != "null"):
                found = True
                print(( "Rotors %s, ring %s, message key was %s, using crib %s" % (rotor_setting, ring_setting, start_pos, cribtext) ))

Lastly, we can tidy up and exit.

        if (found == False): print( 'Attack unsuccessfull' )

        cluster.print_status()
        cluster.close()


### Advanced coding challenge
Use the stanadlone code and these code fragments to assemble a working Python 3 app for OctaPi that distributes the 'find_rotor_start()' function acrross your OctaPi servers. Run it on a selection of crib texts and Enigma cipher text you have created with Py-enigma.

Our code for doing this is [here](source/enigma_bf_canonical.py).

  ![Running pyenigma to create messages](images/enigma-pyenigma-encoding.png)

  ![Running enigma_bf_canonical](images/enigma-canonical-qjf.png)

### Question
If you run the OctaPi code with different ring settings, did you sometimes get more than one result? Why is this?

### Answer
You should have sometimes found multiple valid machine settings for the same rotor selections but with different rotor slip settings and rotor start positions. For example you could have found start position "ABC" with "1 1 1" and "ABD" with "1 1 2". This isn't a bug: both machine settings are valid. In fact there are multiple valid machine settings because the rotor slip ring creates multiple equivalent crypt solutions. This isn't another example of a mistake in the Enigma encryption technique, but shows how the nature of the cyber threat has changed in the 75 years since WWII. Originally, the risk was percieved to be from people successfully decrypting letter by letter. Changing the rotor slip ring meant that the rotors advanced at unexpected positions creating a discontinuity every 26, 26x26 and 26x26x26 chacaters; meaning that an attacker would have to keep starting again. With our Raspberry Pi based crypt attack using a simple brute force exhaust search over full range of possible machine settings, we find that the rotor slip ring setting creates multiple valid solutions. So for us, this feature is a weakness because less searching is needed to reach a valid solution.

Here's an example (compare with the screenshot above).

  ![Running enigma_bf_canonical](images/enigma-canonical-qjg.png)

We could have saved a lot of time coding the slip ring search had we thought of this beforehand.

### Question
What is the minimum length of crib text needed to obtain the correct machine setting?

### Answer
If you run your code multiple time with less and less crib and cipher text characters, you should find that as few as four characters of crib text is enough to obtain the correct machine setting (there could be a handful of incorrect solutions as well). With less than four characters, there is soo much ambiguity that you will have trouble finding the correct solution amongst all the incorrect solutions.

### Very advanced coding challenge
If you have got this far, you could try coding the search over plug board settings. Before you start, try estimating if this is going to be achievable - even with an OctaPi cluster?
