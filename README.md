# Nvidia AutoVM Updater For Hyper-V

![Thumbnail](https://lh3.googleusercontent.com/pw/AM-JKLUJDLBkOcwMW3nvWzlUpLfa3HVdoUWsQe01jNI1xckhizcJBroMQcIWsSQ7AfdhO6G6j8B-8Bf9ystsfqRNVZOre4s-WdYcLL9Yc1TKWYkCwX0it7HsTZEzWSokMBhff1akJ4uB8CIjR2YCB83IdXd9DQ=w990-h718-no?authuser=0)

## What Does this do?
This tool is meant to ease the process for vGPU partitioned VM's by automating the labor of moving files & directories from a host machine to VM's every time you update your graphics drivers. This is otherwise annoying as whenever updating Nvidia drivers, you have to copy the new folders and DLL files from your hosts System32 and place them in every VM individually. This aims to fix that completely on both old and newly created VM's. The original steps are listed in the later part of the instructions on this Reddit post which you can find [**here**](https://www.reddit.com/r/sysadmin/comments/jym8xz/gpu_partitioning_is_finally_possible_in_hyperv/).

## Tips & Disclaimers:
_I recommend taking the time to read the explanation first; as it tends to help avoid confusion should you get lost while reading the steps. Keep in mind that these scripts **DO NOT** create new VM's with vGPU support; instead this assumes you have setup your Windows 10 or higher VM(s) with vGPU partitioned as specified in the Reddit post above._

## Explanation:
This script has a **Host** and **VM** script that work in unison. Both use Windows built-in **Task Scheduler** to push and pull files from a shared folder on your host to your VM's. Below is explaining how both work:

## Host Script:
The Host scripts can be located anywhere on your host computer and runs on startup, however this can be changed to any trigger using **Task Scheduler**. `AutoHostUpdater.bat` calls on `autohost-updater.py` and copies the following `Nv*.dll` files, and Nvidia display folder. Pasting them into a Shared folder you create:

**.DLL Files:** 

    NvAgent.dll
    nvapi64.dll
    nvaudcap64v.dll
    nvEncodeAPI64.dll
    nvcuda.dll
    NvFBC64.dll
    NvIFROpenGL.dll
    nvcuvid.dll
    ffff

**Nvidia Display Folder:** 

    nv_dispi.inf_amd64_000000...

**NOTE:**

_This list can be modified to include more files or directories needed for other drivers that need to match with the host machine. You can do this by editing the list in `needed_dlls` in `autohost-updater.py` & `autovm-updater.py`. **So long as both lists are identical on both the Host and VM scripts, it should work.**_

**WARNING:**

> **DO NOT STORE ANYTHING IMPORTANT IN THE HUB FOLDER AS IT WILL BE DELETED & RECREATED UPON REBOOT!**

## VM Script:
Basically the reverse of the Host script; the VM Script deletes the old files and folders aforementioned in the list above from System32 on your VM, and replaces them with the newly copied files and folders stored in your **hub** folder which is kept updated by the host script. For easy deployment in **Task Scheduler**, `AutoVMUpdater.bat` just calls on `autovm-updater.py`.

## Install Script (**Coming Soon!**):

## Instructions:
_Assuming you followed the Reddit [**post**](https://www.reddit.com/r/sysadmin/comments/jym8xz/gpu_partitioning_is_finally_possible_in_hyperv/) and now have a fully vGPU partitioned VM. We can now setup the graphic driver automation between them using these scripts._

1. First download or clone the GitHub repository on your **Host** machine - This can be anywhere.
2. Create a [**Share**](https://pureinfotech.com/setup-network-file-sharing-windows-10/) folder for which you would like to be the **hub** for the scripts to push and pull files from - This can also be anywhere.
3. Next, open `autohost-updater.py` in the repository you downloaded with the IDE of your choosing - **notepad works too**. 
4. Paste the Share path of the **hub** folder you created in step 2 into the `sharepath` variable.
5. You will need to do step 4 again for `autovm-updater.py` - Such that they both point to where the **hub** folder is.
6. Continuing...

