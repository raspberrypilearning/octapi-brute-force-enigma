## Encrypt a message

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
