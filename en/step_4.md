## Decrypt a message

Imagine you are an Enigma operator and you've just received the message: "YJPYITREDSYUPIU". Let's write some code to use Py-enigma to decrypt it.

+ Open IDLE and create a new file. Save it as `decrypt.py`

[[[rpi-gui-idle-opening]]]

+ First, import the `EnigmaMachine` class from `Py-enigma`. Add this code to your file:

```python
from enigma.machine import EnigmaMachine
```

You consult your Enigma settings sheet and find out that the machine that encrypted the message had the following settings at the time the message was sent:

![Decrypt settings](images/decrypt-settings.png)

+ In your Python file, set up an Enigma machine object. Use the same settings as on your settings sheet, exactly as they appear:

```python
machine = EnigmaMachine.from_key_sheet(
   rotors='',
   reflector='B',
   ring_settings='',
   plugboard_settings='')
```

+ Add some code to set the initial position of the Enigma machine rotors to U, Y and T, to match the sending machine.

```python
machine.set_display('UYT')
```

We were sent "PWE" as the encrypted key for this message. It was encrypted before sending to prevent an eavesdropper from being able to read it. However, our Enigma machine can recover the actual message key used by decrypting "PWE" using the rotor start position we just set: U, Y and T. We then reset the Enigma machine's rotor starting positions with the decrypted message key.

```python
msg_key = machine.process_text('PWE')
machine.set_display(msg_key)
```

We are now ready to decrypt the message. If the message text we received was "YJPYITREDSYUPIU", we can decrypt it using the following:

    ciphertext = 'YJPYITREDSYUPIU'
    plaintext = machine.process_text(ciphertext)

    print(plaintext)

If all is well, you should see the Python 3 script exit without error with "THISXISWORKING".
