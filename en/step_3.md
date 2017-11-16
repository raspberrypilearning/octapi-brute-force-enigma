## What is Enigma, and how does it work?

Enigma is a cipher machine that was created in the early 20th century for commercial, diplomatic, and military applications. The machine was adopted by the German military during World War II for secret communications. The Enigma encryption code was famously broken at Bletchley Park, the forerunner of GCHQ, during WWII, meaning intercepted radio messages from the German military could be decoded and read. This spectacular achievement is thought to have shortened the war, saving many lives on both sides of the conflict.

From an electrical point of view, the Enigma machine is simply a battery, a bulb, and a switch circuit. It doesn't have any electronics, so it is an electro-mechanical device. Encryption is achieved by varying the path of an electric current through the wiring of the machine.

![Encoding a W as G on Enigma](images/Enigma-wiring.gif)

In the diagram above, we show how a character on the keyboard goes through many stages of transposition before being routed to a lightbulb on the lamp board representing the encrypted letter. The user types their plain text message on the keyboard character by character, and reads the cipher text as each bulb is illuminated on the lamp board in response.

Let's look at the rotors and the reflector first.

### Rotors and reflector

Inside the machine, a number of rotors with 26 contacts (one for each letter from A to Z) are stacked together to create the current path through the heart of the machine. Each rotor wheel has electrical contacts on both sides and a jumble of wiring between them, so that the letters are transposed from one side to the other.

![Close-up view of rotor from a WWII captured Enigma machine](images/7X5A0921-closeup.png)

In the photo above, you can see the jumble of wiring inside an expanded rotor wheel from a WWII-captured Enigma machine. By stacking several rotors and using a reflector at the end to return the current back through the rotors, many transpositions per letter can be achieved. This makes it almost impossible to read the text.

### Selecting rotors

When using the Enigma machine, three rotors are selected from five available ones (there were also machines with four rotors). The bottom-most rotor advances as the message is typed, so that a different transposition of letters is used character by character. After the first rotor has advanced 26 positions, the machine advances the next rotor by one, and so on.

### Slip rings

It is also possible to slip round the letter assignments on the side of the rotor wheel so that A = B, or A = C, etc. Changing the point at which the rotors advance makes the encryption sequence discontinuous.

### Plugboard

As if this wasn't enough, a plugboard (the leftmost green box in the diagram at the top) was added to the original design which allows up to ten pairs of letters to be manually transposed as they go into the rotors and again when they come back out.

### Encryption settings

Combining three rotors from a set of five, the rotor settings with 26 positions, and the plugboard with ten pairs of letters connected, the Enigma machine used by WWII military had 158962555217826360000 (nearly 159 quintillion) different settings.

The encryption relied on both the sending and receiving Enigma machines being set the same. To do this, a settings sheet was used at both communicating stations. The sheet specified:
- Which rotors (of those available) should be selected, and in what order they should be inserted into the machine
- How much each rotor should be slipped round
- Which letters should be changed by the plugboard
- Which rotor start position should be used

### Rotor start position and one-off key

A different set of machine settings was used each day, and the rotor start position was changed every six hours, so the machine setting was very time-sensitive. The user also selected three characters for themselves as a one-off message key for each message sent.

![A captured Enigma settings sheet held by GCHQ](images/Enigma-settings-sheet.jpg)

This is an Enigma settings sheet captured at the end of WWII which has been released by GCHQ for this project. In the expanded view of one of the lines shown below, you can see how the various settings are laid out:

![A line of settings from a WWII captured Enigma settings sheet](images/Enigma-settings-line.jpg)

The settings we've highlighted are for the first day of the month, hence the '1' in the second column. The next column shows that rotors IV, I, and V should be selected and used in that order. The fourth column holds the slip ring settings: rotor IV should be slipped round to position 20 (A = T), rotor I to 5 (A = E) and rotor V to position 10 (A = J). Next comes the plugboard wiring: S to X, K to U, Q to F, and so on. Finally, the start position for the rotors should be "SRC", "EEJ, "FNZ", or "SZK" for each 6-hour period of the day.

There were two reflectors used, B or C. These have fixed transpositions of letters, which ensure that the current returns back through the machine without it reversing the transposition on the return leg. We will assume reflector B has been used.
