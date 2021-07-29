# Nvidia AutoVM Updater For Hyper-V

## What Does this do?
This tool is meant to ease the process for vGPU passthough for VM's by automating the labor of moving files & directories from a host machine to VM's everytime you update your graphics drivers. This is otherwise annoying as whenever updating Nvidia drivers, you have to copy the new folders and DLL files from your hosts System32 and place them in every VM individually. This aims to fix that completely on both old and newly created VM's. The original steps are listed in the later part of the instructions on this Reddit post which you can find [**here**](https://www.reddit.com/r/sysadmin/comments/jym8xz/gpu_partitioning_is_finally_possible_in_hyperv/).

## Tips & Disclaimers:
_I recommend taking the time to read the explanation first; as it tends to help avoid confusion should you get lost while reading the steps. Keep in mind that these scripts **DO NOT** create new VM's with vGPU support; instead this assumes you have setup your Windows 10 or higher VM(s) with vGPU partitioned as specified in the Reddit post above._

## Explanation:
This script has a **parent** and **child** script that work in unison. Below is explaining how both work:

### Parent Script:



### Child Script:


## Instructions:
Assuming you followed the Reddit post and now have a fully vGPU passthrough VM; Now we can 
