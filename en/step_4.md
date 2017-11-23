## Enigma during WWII

In WWII, Enigma-encrypted messages were usually sent in Morse code via shortwave radio. This means they could easily be intercepted some distance away, so the German military relied heavily on the strength of the encryption technique to keep their messages secret. However, Britain intercepted and successfully decrypted the messages at Bletchley Park.

An Enigma-encrypted transmission would have looked similar to this:

![Encrypted message](images/encrypted-message.png)

How did operators at communications stations go about encrypting?

### Step 1: Select the rotors and choose a three-letter message key
First, the operator found the line on the settings sheet that corresponds to the current day of the month. This told her how to set the Enigma machine, including which rotors to select and in what order to put them, as well as the rotor start position for the current six-hour period.

### Step 2: Choose and encrypt a three-letter message key
The operator then picked a one-off three-letter message key, which should be random and unique to every single message. Let's say she thought of "SCC" as the key. Obviously, this key could not be sent openly. To encrypt it for transmission, the operator typed "SCC" into the Enigma machine she had set according to the sheet, and obtained (for example) "PWE" as the encrypted key. This key was then safe to send over a radio channel.

For at least part of WWII, the German military procedure was to send and encrypt the message key twice. Using our example, the operator would have typed "SCCSCC" and obtained "PWEHVF".

**There is a flaw with repeating the message key — what is it?**

--- collapse ---
---
title: Answer
---
We previously said that no plain-text letter gets encrypted as itself. This means that anyone who intercepts an Enigma-encoded message knows that none of the letters in the decrypted message key can possibly be the right ones. In our example, intercepting the key "PWE" tells us that "P" is **not** the first letter, "W" is **not** the second, and "E" is **not** the third.

If the message key is sent twice, as German military used to do, we also know the first letter cannot be "H", the second can't be "V", and the third can't be "F". This reduces the amount of searching we need to do to find the plain-text letters of the message key, because we can already exclude two options for each letter in the key.

--- /collapse ---

### Step 3: Encrypt the message using the unencrypted message key
Once the message key was chosen and encrypted, the operator set the rotors to the unencrypted version of the key that she had chosen, and typed the message into the keyboard.

Numbers had to be spelled out in full, because the Engima machine doesn't have number keys. There was also no space bar, so a space was often indicated by an 'X'. For example, if we wanted to encrypt "this message is secret", we would type in "THISXMESSAGEXISXSECRET".

### Step 4: Send the encrypted message via radio
A radio operator would then send the message in Morse code, using call signs and abbreviated text, just as we use abbreviations in text messages to reduce the amount of typing needed.
