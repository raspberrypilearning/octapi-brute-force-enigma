## Enigma during WWII

In WWII, Enigma-encrypted messages were usually sent in Morse code via shortwave radio. This means they could easily be intercepted some distance away, so the military relied heavily on the strength of the encryption technique to keep their messages secret. However, Britain intercepted and successfully decrypted the messages at Bletchley Park.

An Enigma-encrypted transmission would have looked similar to this:

![Encrypted message](images/encrypted-message.png)

How did operators at communications stations go about encrypting?

### Step 1: Select the rotors and choose a three-letter message key
The operator would find the line on the settings sheet that corresponds to the current day of the month. The first thing on the settings sheet is which rotors to use and in what order to use them. The rotor start position for the current six-hour period is at the end of the line. The operator then chooses a one-off three-letter message key, which should be unique to every message. Obviously, this key could not be sent openly, so it was encrypted for transmission.

Example:
Assume the settings sheet tells the operator to select rotors II, V and III, and insert them into the machine left to right with the starting positions U, Y, and T. She thinks of "SCC" as the message key, choosing the letters at random.

### Step 2: Encrypt the message key
When the operator types "SCC" on the Enigma keyboard with these settings, she obtains "PWE" as the encrypted form of the message key. This key is now safe to send over a radio channel.

For at least part of WWII, the German military procedure was to send and encrypt the message key twice. Using our example, the operator would have typed "SCCSCC" and obtained "PWEHVF".

**There is a flaw with repeating the message key — what is it?**

--- collapse ---
---
title: Answer
---
We previously said that no plain-text letter gets encrypted as itself. This means that anyone who intercepts an Enigma-encoded message knows that none of the letters in the decrypted message key can possibly be the right ones. In our example, intercepting the key "PWE" tells us that "P" is **not** the first letter, "W" is **not** the second, and "E" is **not** the third.

If the message key is sent twice, as German military used to do, we also know the first letter cannot be "H", the second can't be "V", and the third can't be "F". This reduces the amount of searching we need to do to find the plain-text letters, because we can already exclude two options for each letter in the key.

--- /collapse ---

### Step 3: Encrypt the message using the unencrypted message key
Once the message key was chosen and encrypted, the operator set the rotors to the unencrypted version of the key that she chose, and typed the message into the keyboard. Numbers had to be spelled out in full, because the Engima machine doesn't have number keys. A space was often indicated by an 'X', because there was no space bar.

So if we wanted to say "this message is secret", we would type "THISXMESSAGEXISXSECRET".

### Step 4: Sending the encrypted message via radio
A radio operator would then send the message in Morse code, using a series of callsigns and abbreviated text, just as in modern-day text messages we use abbreviations to reduce the amount of typing needed.
