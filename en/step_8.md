## Crypt attack using OctaPi

This part of the resource requires an [OctaPi cluster](https://projects.raspberrypi.org/en/projects/build-an-octapi).

Before you begin, you will need to install Py-Enigma on your client machine and all the servers in your OctaPi cluster.

--- collapse ---
---
title: Install Py-Enigma on the OctaPi client and servers
---

+ Boot up the client and connect it to the Internet. This will mean disconnecting from your OctaPi router and connecting to your Wi-Fi network for internet access.

+ Open a terminal window

![Open a terminal](images/terminal.png)

+ Type the following commands into the terminal

```bash
sudo pip3 install py-enigma
sudo pip3 --upgrade py-enigma
```

+ Disconnect the OctaPi client from the internet and re-connect it to your dedicated OctaPi router.

+ Remove any entries in `wpa_supplicant` that are for Wi-Fi networks other than OctaPi to avoid the client connecting to the wrong network.

In a terminal window, type the following command to edit the `wpa_supplicant.conf` file:

```bash
sudo nano \etc\wpa_suplicant\wpa_suplicant.conf
```

+ Press `Ctrl` + `o` to save and `Ctrl` + `x` to exit the text editor.

Next, repeat this process for each of the servers.

+ Select one server, then connect a keyboard, screen and mouse to it so that you can administer it directly from a terminal window.

+ Repeat all the steps needed to install Py-enigma that you followed for the client.

+ Remember to remove any entries in `wpa_supplicant` that are for Wi-Fi networks other than OctaPi

+ Shut down the server and either repeat the installation the same way for the rest of the servers in your cluster, or replicate the SD card

--- /collapse ---

To do an exhaustive search of all rotor slip ring settings, we will need to run a lot of jobs on OctaPi using Dispy, which you installed when you built the OctaPi. The OctaPi code using Dispy is very similar to the code we created for a standalone processor.

The demand on the OctaPi client machine for memory will be quite large, so we will need to run the program one ring setting at a time.

+ Start with the code you wrote for the standalone attack, but save a copy of the file as `bruteforce_octapi.py`. Remove the loop in the main part of the program but keep all of the variables and the function `find_rotor_start()`.

+ Alter the `find_rotor_start()` function so that it now takes an additional parameter - the `ring_choice`. This will be a string containing 3 numbers separated by spaces, for example "1 1 1".

+ Inside the function, set the ring choice in the Enigma machine object to be the ring choice that was passed into the function as a parameter.

+ Find the two places where a value is returned from the function (when a match has been found, or when all possibilities are exhausted and no match was found). In addition to returning the rotor choice and start position, add code to additionally return the `ring_choice` so that three values in total are returned from the function. The `ring_choice` should be the second value returned.

+ In the main part of your program (where your loop originally was in the standalone version), instead create a cluster object on the OctaPi network like this. If your OctaPi network uses a different IP address range to the default, you will need to alter the code to reflect this.

```python
cluster = dispy.JobCluster(find_rotor_start, nodes='192.168.1.*')
jobs = []
id = 1    
```

+ Add some code to allow the user to input the cipher text, the crib text and the slip ring setting. You could either do this via the `input()` function or by collecting the arguments from the command line with the `argparse` module.

+  Submit the `find_rotor_start()` jobs to the cluster using a similar method to the loop we used in the standalone brute force attack.

```python
# Submit the jobs for this ring choice
for rotor_choice in rotor:
    job = cluster.submit( rotor_choice, ring_choice, ciphertext, cribtext )
    job.id = id # Associate an ID to the job
    jobs.append(job)
    id += 1   # Next job
```

+ Next we need to wait for the jobs to complete before collecting the results returned from the cluster.

```python
print( "Waiting..." )
cluster.wait()
print( "Collecting job results" )
```

+ The last step is to sift through the results to see if any of the `find_rotor_start()` jobs didn't return the string `"Cannot find settings"`, in which case the returned string must have been a valid rotor start position.

```python
# Collect and check through the jobs for this ring setting
found = False
for job in jobs:
    # Wait for job to finish and return results
    rotor_setting, ring_setting, start_pos = job()

    # If a start position was found
    if (start_pos != "Cannot find settings"):
        found = True
        print(( "Rotors %s, ring %s, message key was %s, using crib %s" % (rotor_setting, ring_setting, start_pos, cribtext) ))
```

+ Lastly, we can tidy up and exit.

```python
if (found == False):
    print( 'Attack unsuccessful' )

cluster.print_status()
cluster.close()
```


### Advanced coding challenge
Use the stanadlone code and these code fragments to assemble a working Python 3 app for OctaPi that distributes the 'find_rotor_start()' function acrross your OctaPi servers. Run it on a selection of crib texts and Enigma cipher text you have created with Py-enigma.

Our code for doing this is [here](source/enigma_bf_canonical.py).

  ![Running pyenigma to create messages](images/enigma-pyenigma-encoding.png)

  ![Running enigma_bf_canonical](images/enigma-canonical-qjf.png)

### Question
If you run the OctaPi code with different ring settings, did you sometimes get more than one result? Why is this?

### Answer
You should have sometimes found multiple valid machine settings for the same rotor selections but with different rotor slip settings and rotor start positions. For example you could have found start position "ABC" with "1 1 1" and "ABD" with "1 1 2". This isn't a bug: both machine settings are valid. In fact there are multiple valid machine settings because the rotor slip ring creates multiple equivalent crypt solutions. This isn't another example of a mistake in the Enigma encryption technique, but shows how the nature of the cyber threat has changed in the 75 years since WWII. Originally, the risk was percieved to be from people successfully decrypting letter by letter. Changing the rotor slip ring meant that the rotors advanced at unexpected positions creating a discontinuity every 26, 26x26 and 26x26x26 chacaters; meaning that an attacker would have to keep starting again. With our Raspberry Pi based crypt attack using a simple brute force exhaust search over full range of possible machine settings, we find that the rotor slip ring setting creates multiple valid solutions. So for us, this feature is a weakness because less searching is needed to reach a valid solution.

Here's an example (compare with the screenshot above).

  ![Running enigma_bf_canonical](images/enigma-canonical-qjg.png)

We could have saved a lot of time coding the slip ring search had we thought of this beforehand.

### Question
What is the minimum length of crib text needed to obtain the correct machine setting?

### Answer
If you run your code multiple time with less and less crib and cipher text characters, you should find that as few as four characters of crib text is enough to obtain the correct machine setting (there could be a handful of incorrect solutions as well). With less than four characters, there is soo much ambiguity that you will have trouble finding the correct solution amongst all the incorrect solutions.

### Very advanced coding challenge
If you have got this far, you could try coding the search over plug board settings. Before you start, try estimating if this is going to be achievable - even with an OctaPi cluster?




We will run the program using command line arguments in order to set the cipher text, crib text and rotor slip ring settings at run time. If our Python code is called 'enigma_bf_canonical.py', the command line will look like:

    sudo python3 enigma_bf_canonical.py 'FKFPQZYVON' 'CHELTENHAM' '1 1 1'

 Where
     'FKFQQZYVON' is cipher text produced by an Enigma machine, or the pyenigma.py utility
     'CHELTENHAM' is text that was encrypted, we are using it as a crib
