## Enigma during WWII

In WWII, Enigma messages were normally sent in Morse code via shortwave radio. This means they could easily be intercepted some distance away, so the military relied heavily on the strength of the encryption technique to keep their messages secret. However, Britain intercepted and successfully decrypted the messages at Bletchley Park.

A number of different radio procedures were used by the different parts of the German military, but they all worked in a similar way (we assume the machines have been set the same from the machine setting sheet). This is what we would have received if we were intercepting an Enigma-encrypted transmission.

### Step 1: Select the rotors and choose a three-letter message key
The operator would find the line on the settings sheet that corresponds to the current day of the month. The first thing on the settings sheet is which rotors to use and in what order to use them. The rotor start position for the current six-hour period is at the end of the line. The operator then chooses their own three-letter message key which should be unique to every message. Obviously, this key could not be sent openly, so it was encrypted for transmission.

Example:
Assume the settings sheet tells the operator to select rotors II, V and III, and insert them into the machine left to right with the starting positions U, Y, and T. She thinks of "SCC" as the message key (choosing it at random).

### Step 2: Encrypt the message key
When the operator types "SCC" on the Enigma keyboard with these settings, she obtains "PWE" as the encrypted form of the message key. This key is now safe to send over a radio channel.

For at least part of WWII, the German military procedure was to send and encrypt the message key twice. Using our example, they would have typed "SCCSCC" and obtained "PWEHVF".

**There is a flaw with repeating the message key — what is it?**

--- collapse ---
---
title: Answer
---
We previously observed that no plain text letters get encrypted as themselves. This means that we know that the message key cannot possibly be "P" for the first letter, "W" for the second, or "E" for the third. In addition if the message key is sent twice, we also know it cannot be "H", followed by "V" followed by "F". This reduces the amount of searching required to find the plain text letters, because the first letter is neither "P" or "H", and so on.

--- /collapse ---

### Step 3: Encrypt the message using the unencrypted message key
Once the message key was chosen and encrypted, the machine was reset to the unencrypted version of the key that the operator chose, and the message was typed into the keyboard. Numbers had to be spelled out in full (because there were no number keys). A space was often indicated by the letter 'X', because there was no space bar.

So if we wanted to say "this is working", we would type "THISXISXWORKING".

### Step 4: Sending the encrypted message via radio
A radio operator would then send the message in Morse code, using a series of callsigns and abbreviated text, just as in modern-day text messages we use abbreviations to reduce the amount of typing needed.
