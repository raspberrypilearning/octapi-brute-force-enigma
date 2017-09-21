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
