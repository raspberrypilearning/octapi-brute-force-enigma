## Decrypt a message

Imagine you are an Enigma operator and you've just received this message:

![Encrypted message](images/encrypted-message.png)

Let's write some code using `Py-enigma` to simulate using an Enigma machine to decrypt the message.

+ Open IDLE, create a new file, and save it as `decrypt.py`.

Consulting your Enigma settings sheet, you find out that the encrypting machine had the following settings at the time it sent the message:

![Decrypt settings](images/decrypt-settings.png)

+ Inside your file, import the `EnigmaMachine` class, and set up the `machine` with the settings shown on the settings sheet. Like last time, use reflector B.

+ Add some code to set the initial positions of the rotors to `U`, `Y`, and `T` to match the sending machine.

The other operator sent you "PWE" as the key for this message. Before sending, the key was encrypted to prevent an eavesdropper from being able to read it.

You first need to use your Enigma machine to recover the **actual** message key by decrypting "PWE" using the settings sheet's rotor start positions: `U`, `Y`, and `T`.

+ Add the following code to decrypt the key, and run your program to display the decrypted key:

```python
# Decrypt the text 'PWE' and store it as msg_key
msg_key = machine.process_text('PWE')
print(msg_key)
```

+ Add some code at the bottom of the program to set the Enigma machine's rotor starting positions to the decrypted message key you just obtained.

--- hints ---
--- hint ---
Look at how you originally set the rotor positions to `UYT`, and see if you can use this code to set the rotor positions to the new setting.
--- /hint ---
--- hint ---
Here is how your code should look:

```python
# Set the new start position of the Enigma rotors
machine.set_display(msg_key)
```
--- /hint ---
--- /hints ---

You are now ready to decrypt the message.

+ Write some code to decrypt the cipher text.

--- hints ---
--- hint ---
This code will be very similar to the code you used to decrypt the key. Create a **variable** to store the result, use the `machine` to process the cipher text, and then `print` the result.
--- /hint ---
--- hint ---
Here is how your code should look:

```python
ciphertext = 'YJPYITREDSYUPIU'
plaintext = machine.process_text(ciphertext)

print(plaintext)
```
--- /hint ---
--- /hints ---

--- collapse ---
---
title: What is the decrypted message?
---
If all is well, you should see the script exiting without any errors, and the decrypted message "THISXISXWORKING".

--- /collapse ---


**What do you notice about the processes of encrypting and decrypting text?**

--- collapse ---
---
title: Answer
---
They are exactly the same! The code you wrote in this section is identical to the code you wrote to encrypt the message.

--- /collapse ---
