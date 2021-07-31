from os import getenv, remove, rmdir, walk, mkdir, system
import os
from shutil import copy2, rmtree, copytree

print(os.environ['HOSTVM'])



'''

powershell.exe Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Virtual Machine\Guest\Parameters" | Select-Object HostName
echo HOSTVM%
'powershell "$env:HostVM"'

sharepath = "//Quantum7/Share/Cuda_Drivers/" # Edit to path of Share drive
syspath = "C:/Windows/System32/"
check = "nv_dispi.inf_amd64_"
folders = []
direc = []
dlls = []
existing = []
needed_dlls = {
   'NvAgent.dll',
   'nvapi64.dll',
   'nvaudcap64v.dll',
   'nvEncodeAPI64.dll',
   'nvcuda.dll',
   'NvFBC64.dll',
   'NvIFROpenGL.dll',
   'nvcuvid.dll'
}

# What directory exists in FileRepository:
for (dirpath, dirnames, filenames) in walk(syspath+'HostDriverStore/FileRepository/'):
    direc.extend(dirnames)
    nvidiafilepres = [i for i in direc if i.startswith(check)]
    try: existing = nvidiafilepres.pop()
    except: continue

# Get a list current files and directory's in Share drive:
for (dirpath, dirnames, filenames) in walk(sharepath):
    dlls.extend(filenames)
    folders.extend(dirnames)
    nvidiafile = [i for i in folders if i.startswith(check)]
file = nvidiafile.pop()

# Removing the existing folder if not the same as in sharepath:
if file != existing:
    try: [rmtree(syspath+'HostDriverStore')]
    except: [print("Removed old files...")]
else: [print("Already Updated - Nothing to do.")] [exit(0)]

# Try to delete old Nvidia DLL files in System32:
for i in needed_dlls:
    try: [remove(syspath+i)]
    except: [print("Couldn't find: "+i+" in "+syspath)]
    copy2(str(sharepath+i), str(syspath)) # Copy new Nvidia DLL files from Share drive
print("Copied new Nvidia DLL files from: "+sharepath)
copytree(str(sharepath+file), str(syspath+"HostDriverStore/FileRepository/"+file))
print("Copied: "+file+" to "+syspath+"\nCompleted.") [exit(0)]
'''
