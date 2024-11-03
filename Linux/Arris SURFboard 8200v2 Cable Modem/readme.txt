The Arris SURFboard SB8200v2 cable modem does not have a built-in way to schedule automatic reboots. Thankfully, with a combination of Python, Selenium, and crontab, there is a way schedule automatic reboots. Unfortunately, this is a rather convoluted solution, and it may not work for every use case. This has only been tested on the Arris SURFboard SB8200v2 cable modem, but the underlying principles may be applicable/tweakable for other makes and models. 


There are several key parts to this solution:

• The IP addressing schema
• The availability of the second WAN port on the SB8200v2
• Physical connectivity between the SB8200v2 and the Linux computer running these scripts
• Permissions on the Linux computer running these scripts
• The limitations of cron jobs


To set the stage for this solution, I will run through my particular use case. I have only successfully connected to my SB8200v2's web interface whenever I have a computer connected directly to its second WAN port (the RJ45 port labeled "2"). Although the modem uses the IP addressing scheme of 192.168.100.1/24, I could never successfully connect to it while my computer was connected to a router (even with the router on that same IP addressing scheme). In other words, I had to connect my computer to the second WAN port with an ethernet cable and manually configure my computer's IP address to 192.168.100.2/24 just to connect to the SB8200's web interface. This makes it much more difficult to access the SB8200's web interface quickly. Although I most often use the web interface to safely reboot my modem (physically removing its power source often makes me nervous about its longevity), I also use it to check the status of the upstream and downstream bonded channels. 

Instead of changing over my ethernet cables and manually reconfiguring my IP address each time, I took a different approach. I already had a Proxmox server inches away from my SB8200, so I set up a Debian Linux virtual machine dedicated for just this task (XFCE desktop environment, 1 CPU core, 1 GB of RAM, 20 GB drive). Thanks to Proxmox's USB passthrough feature, I used a TP-Link USB 3.0 NIC and manually set that to 192.168.100.2/24 (if your Proxmox server has multiple integrated NICs, one of those could be passed through to the guest VM as well). An older laptop or desktop would work in this scenario as well, but I prefer a Proxmox VM for easier access to the console.

This solved my web interface access issue, but its lack of features left me disappointed. The web interface has very few options and is mainly useful just for checking the SB8200's status and rebooting it. There are no options to enable SSH access, no options to schedule automatic reboots, or anything else that usually grabs the attention of IT administrators. With my particular SB8200, a weekly reboot is almost mandatory. Although most websites and video streaming services work fine, voice calls and video conferences (of all the major platforms) have more dropouts and stuttering the longer I go in between modem reboots (and accompanying router reboots). A manual reboot only takes a few minutes of my time, but it's such a simple task that doing it manually every week feels like a crime. After much thought, I asked myself "Is there a way in Debian to automatically open Firefox and have it click a few buttons for me?" As you can tell by the existence of this solution, the answer is "yes."

Using Python and Selenium, I was able to automatically open Firefox, navigate to the SB8200's web interface, log in with the modem's credentials, and automatically navigate through the web interface (by checking the page source for the items I needed to click) to initiate a reboot. With the difficult part out of the way, I assumed scheduling a cron job for this would be simple. It turns out that cron much prefers CLI tasks and opening Firefox through Python only added to that challenge. Thankfully, I found a workaround which uses a Bash script that will automatically execute my Python script. This adds an extra step to the process, but it makes the cron job much simpler. There may be a more efficient approach to this, but I was just happy to see complete functionality at the time.


When setting up a Debian (or other Linux distro that uses apt) computer for this solution, I would highly recommend running the following commands before changing its IP address/isolating it to the modem's subnet:

Check for software updates: sudo apt update
Install software upgrades: sudo apt upgrade
Install Python 3: sudo apt install python3
Install Selenium for Python 3: sudo apt install python3-selenium
To avoid dependency/missing software issues, it may be wise to install a Python IDE such as Eric
Install any other software you think you may need


After creating the scripts and/or putting them in your preferred directory, I would recommend running the following commands:

Make the script executable: sudo chmod +x /path/to/script
Change the ownership of the script (if needed): sudo chown username /path/to/script


Also, be sure to make the following changes to the .sh and .py scripts:

.sh script: It may be more efficient to rename it to something simpler (I use "modem-reboot.sh")
.sh script line 3: Change the username to match the username running the script
.sh script line 5: Change the path to the .py script (I use "/scripts/modem-reboot.py)
.py script line 13: Verify the URL for your modem's web interface and change it if needed
.py script line 20: Verify your modem's username and change it if needed
.py script line 24: Verify your modem's password and change it if needed
.py script line 34: Verify the URL for the CONFIGURATION page and change it if needed


This solution is a bit convoluted, but my goal of sharing this is to help out at least one other person who was in this same situation. With some minor tweaks, this solution should work for other Linux distros. I would highly recommend renaming the Python and Bash scripts to something shorter and more straightforward in practice (i.e. "modem-reboot.py"). This was a fun project and it feels good to have another chore fully automated.