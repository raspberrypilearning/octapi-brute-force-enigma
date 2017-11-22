## Encrypt a message

Now let's use your Python-powered Enigma machine to create a secret message!

+ Open IDLE, create a new file, and save it as `encrypt.py`.

[[[rpi-gui-idle-opening]]]

+ First, import the `EnigmaMachine` class from `Py-enigma` by adding this code to your file:

```python
from enigma.machine import EnigmaMachine
```
Consulting your Enigma settings sheet, you find out that the settings for today are as follows:

![Encrypt settings](images/encrypt-settings.png)

+ In your Python file, set up an `EnigmaMachine` object using the settings from your settings sheet. Each setting should be a **string** and should be typed exactly as it appears on the settings sheet. For example, the `rotors` will be set as `'IV I V'`.

```python
# Set up the Enigma machine
machine = EnigmaMachine.from_key_sheet(
   rotors='',
   reflector='B',
   ring_settings='',
   plugboard_settings='')
```

As we said, we'll be using reflector B for all of our programs.

+ Write another line of code to set the rotor start positions to the settings from the sheet.

```python
# Set the initial position of the Enigma rotors
machine.set_display('FNZ')
```

+ Choose three random letters to use as your message key — we will use "BFR", but you can choose whatever you like. Encrypt the message key and make a note of the result. This is the encrypted key you will send with your message.

```python
# Encrypt the text 'BFR' and store it as msg_key
msg_key = machine.process_text('BFR')
print(msg_key)
```

+ Write a line of code to reset the rotor start positions to your **unencrypted** message key (in our example, "BFR").

+ Write some code to process the `plaintext` "RASPBERRYPI" and display the resulting `ciphertext`.

--- hints ---
--- hint ---
Here is the code you used to encrypt the message key "BFR". Can you alter this code to encrypt your plaintext `"RASPBERRYPI"`?

```python
msg_key = machine.process_text('BFR')
```
--- /hint ---
--- hint ---
Here is the code you will need:

```python
plaintext = "RASPBERRYPI"
ciphertext = machine.process_text(plaintext)
print(ciphertext)

```
--- /hint ---
--- /hints ---

If you used the message key "BFR", the resulting ciphertext should be "GON XXLXYFQNZIK". If you've chosen a different message key, your result will be different.

You can also run `pyenigma` from the command line if you wish. If you type this command into a terminal window, it will produce the same result as the script you just wrote.

```bash
pyenigma.py -r IV I V -i 20 5 10 -p SX KU QP VN JG TC LA WM OB ZF -u B --start BFR --text "RASPBERRYPI"
```

**Do any of the characters ever get encrypted as themselves (i.e. does "A" get encrypted as "A", "B" as "B", etc.)?**

--- collapse ---
---
title: Answer
---
No. This is in fact a weakness of the Enigma system, because, as we said, an attacker who wants to break a code can eliminate all possible crypt attack solutions where an "A" is decrypted as an "A", and so on.

--- /collapse ---


### Challenge

+ Try encrypting text using different settings from a real Enigma settings sheet to see how the text changes.

![A captured Enigma settings sheet held by GCHQ](images/Enigma-settings-sheet.jpg)
