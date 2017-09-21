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
