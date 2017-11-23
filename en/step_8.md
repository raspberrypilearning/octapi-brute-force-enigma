## Crypt attack using OctaPi

This part of the resource requires an [OctaPi cluster](https://projects.raspberrypi.org/en/projects/build-an-octapi){:target="_blank"}.

Before you begin, you will need to install `Py-enigma` on your client machine and all the servers in your OctaPi cluster.

--- collapse ---
---
title: Install `py-enigma` on the OctaPi client and servers
---

+ Boot up the client and connect it to the internet. This will mean disconnecting from your OctaPi router and connecting to your WiFi network for internet access.

+ Open the terminal.

![Open a terminal](images/terminal.png)

+ Type the following command into the terminal window:

```bash
sudo pip3 install py-enigma
```

+ Disconnect the OctaPi client from the internet and connect it to your dedicated OctaPi router again.

+ Type the following command into a terminal window to open the `wpa_supplicant.conf` file:

```bash
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

+ To avoid the client connecting to the wrong network, remove any entries in `wpa_supplicant.conf` that are for WiFi networks other than OctaPi.

+ Press `Ctrl` + `o` to save, and `Ctrl` + `x` to exit the text editor.

Next, repeat the following process for each of the servers.

+ Select one server, then connect a keyboard, screen, and mouse to it so that you can administer it directly from a terminal window. Alternatively, place the SD card into a Raspberry Pi with connected peripherals.

+ Repeat all the steps needed to install `Py-enigma` that you followed for the client.

+ Shut down the server and either repeat the installation the same way for the rest of the servers in your cluster, or duplicate the SD card.

--- /collapse ---

To do an exhaustive search of all rotor slip ring settings, we will need to run a lot of jobs on OctaPi using Dispy, which you installed when you built the OctaPi. The OctaPi code using Dispy is very similar to the code we created for a standalone processor.

The demand on the OctaPi client machine's memory will be quite high, so we will need to run the program one ring setting at a time.

+ Start with the code you wrote for the standalone attack, but save a copy of the file as `bruteforce_octapi.py`.

+ Open the file using Python 3 (IDLE) from the **Programming** menu.

+ Remove everything except the list of rotor permutations and the `find_rotor_start()` function.

+ Import `dispy` at the top of the file.

```python
import dispy
```

+ Alter the `find_rotor_start()` function so that it now takes an additional parameter: the `ring_choice`. This will be a **string** containing three numbers separated by spaces, for example `'1 1 1'`.

+ Inside the function, set the `ring_choice` in the `EnigmaMachine` object to be the `ring_choice` that was passed into the function.

+ Find the two places where a value is returned from the function (when a match has been found, or when all possibilities are exhausted and no match was found). In addition to returning the rotor choice and start position, add code to return the `ring_choice` as the **second** value returned, so that the function returns three values in total.

+ In the main part of your program (where your loop was in the standalone version), add some code to allow the user to input the cipher text, the crib text, and the ring setting. You could either do this via the `input()` function or by collecting the arguments from the command line with the `argparse` module.

+ Create a `cluster` object on the OctaPi network using the code below. If your OctaPi network uses a different IP address range to the default, you will need to alter the `nodes` part of the code to reflect this.

```python
cluster = dispy.JobCluster(find_rotor_start, nodes='192.168.1.*')
jobs = []
id = 1    
```

+ Submit the `find_rotor_start()` jobs to the cluster using a similar method to the loop you used in the standalone brute-force attack.

```python
# Submit the jobs for this ring choice
for rotor_choice in rotors:
    job = cluster.submit( rotor_choice, ciphertext, cribtext, ring_choice )
    job.id = id # Associate an ID to the job
    jobs.append(job)
    id += 1   # Next job
```

+ Next we need to wait for the jobs to complete before collecting the results the cluster has returned.

```python
print( "Waiting..." )
cluster.wait()
print( "Collecting job results" )
```

+ The last step is to sift through the results to see if any of the `find_rotor_start()` jobs did not return the string `"Cannot find settings"`, in which case the returned string must have been a valid rotor start position.

```python
# Collect and check through the jobs for this ring setting
found = False
for job in jobs:
    # Wait for job to finish and return results
    rotor_setting, ring_setting, start_pos = job()

    # If a start position was found
    if start_pos != "Cannot find settings":
        found = True
        print( "Rotors %s, ring %s, message key was %s, using crib %s" % (rotor_setting, ring_setting, start_pos, cribtext) )
```

+ Lastly, you can tidy up and exit.

```python
if found == False:
    print( 'Attack unsuccessful' )

cluster.print_status()
cluster.close()
```

+ Save and run your code from a terminal using the ciphertext `'FKFPQZYVON'` with the crib `'CHELTENHAM'` and ring settings `'1 1 1'`. The program should take around 30 seconds to complete.

Here is an example of the program running with arguments passed from the command line:

![Running enigma_bf_canonical](images/enigma-canonical-qjf.png)

**If you run the OctaPi code with different ring settings, do you sometimes get more than one result? Why is this?**

--- collapse ---
---
title: Answer
---

For the same rotor selections, you sometimes find multiple valid machine settings with different ring settings and rotor start positions. For example, you could have found start positions "ABC" with ring settings "1 1 1", as well as "ABD" with "1 1 2", as two valid results. This isn't a bug: both machine settings are valid. In fact, there are multiple valid machine settings because moving the rotor's slip ring creates multiple equivalent crypt solutions.

This isn't another example of a mistake in the Enigma encryption technique, but shows how the nature of the cyber threat has changed in the 75 years since WWII. Originally, the risk was posed by people decrypting letter by letter. Changing the rotor slip ring meant that the rotors advanced at unexpected positions, creating a discontinuity every 26, 26×26 and 26×26×26 characters, meaning that an attacker would have to keep starting again. With our Raspberry Pi–based crypt attack using a simple brute-force exhaust search over the full range of possible machine settings, we find that the rotor slip ring setting creates multiple valid solutions. So for us, this feature is a weakness because less searching is needed to find a valid solution.

Here's an example (compare with the screenshot above):

  ![Running enigma_bf_canonical](images/enigma-canonical-qjg.png)

We could have saved a lot of time coding the slip ring search if we had known this beforehand.

--- /collapse ---

**What is the minimum length of crib text needed to obtain the correct machine setting?**

--- collapse ---
---
title: Answer
---
If you run your code multiple times with fewer and fewer crib and cipher text characters, you should find that as few as four characters of crib text is enough to obtain the correct machine setting (as well as a handful of incorrect solutions). With fewer than four characters, there is so much ambiguity that you will have trouble finding the correct solution amongst all the incorrect solutions.

--- /collapse ---
