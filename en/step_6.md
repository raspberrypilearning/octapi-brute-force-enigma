## Enigma in use during WWII

Enigma messages were normally sent in Morse code over shortwave radio. This means they could easily be intercepted some distance away, so there was heavy reliance on the strength of the encryption technique to keep the messages secret. In the event, it was possible for the messages to be received in Britain and successfully decrypted at Bletchley Park.

Let's have a look at how messages were sent so that we can create a message authentically using Py-Enigma then develop Python code to crypt attack it.

A number of different radio procedures were used by the different parts of the German military, but they all looked a bit like this (we assume the machines have been set the same from the machine setting sheet). This is what we would have received if we were intercepting an Enigma encrypted transmission.

### Step 1: Select the rotors and choose a three character message key
The operator would find the line on the settings sheet that corresponds to the current day of the month. Which rotors to use and in what order is the first thing on the settings sheet. The rotor start position for the current 6 hour period is on the end of the line. The operator chooses a three letter message key which should be unique to every message. This key could not be sent in the clear (for fairly obvious reasons), so it was encrypted for transmission.

Example:
Assume the settings sheet tells us to select rotors, II, V and III and insert them into the machine left to right with the starting positions to U, Y and T. We think of SCC as our message key (choosing it at random).

### Step 2: Encrypt the message key
When we type "SCC" on the Enigma keyboard with these settings, we obtain "PWE" as the encrypted form of the message key. This is safe to send over a radio channel.

In Py-Enigma, we can reproduce this by typing the following into the terminal

```bash
pyenigma.py -r II V III -i 1 1 1 -p AV BS CG DL FU HZ IN KM OW RX -u B --start=UYT --text='SCC'
```

For at least part of WWII, the German military procedure was to send the message key encrypting it twice, in our example they would have typed "SCCSCC" and obtained "PWEHVF".

**There is a flaw with repeating the message key, what is it?**

--- collapse ---
---
title: Answer
---
We previously observed that no plain text letters get encrypted as themselves. This means that we know that the message key cannot possibly be "P" for the first letter, "W" for the second, or "E" for the third. In addition if the message key is sent twice, we also know it cannot be "H", followed by "V" followed by "F". This reduces the amount of searching required to find the plain text letters because the first letter is neither "P" or "H", and so on.

--- /collapse ---

### Step 3: Encrypt the message using the unencrypted message key
Once the message key was chosen and encrypted, the machine was reset to the unencrypted version of the key and the message was typed into the keyboard. Numbers had to be spelled out in full (because there were no number keys), also a space was often indicated by the letter 'X' because there was no space bar.

So if we wanted to say "this is working", we would type "THISXISXWORKING"

In Py-Enigma, this looks like:

```bash
pyenigma.py -r II V III -i 1 1 1 -p AV BS CG DL FU HZ IN KM OW RX -u B --start='SCC' --text='THISXISXWORKING'
```

`YJPYITREDSYUPIU` is the cipher text produced assuming SCC is the unencrypted message key.

### Step 4: Radio operator sends the encrypted message and everything needed for secret decryption (in Morse code)
The radio operators would have sent the message in Morse code using a series of callsigns and abbreviated text, just as in modern day text messages we use abbreviations such as "LOL" and "m8" to reduce the amount of typing needed.
