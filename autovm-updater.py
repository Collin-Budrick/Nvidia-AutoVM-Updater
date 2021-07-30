from os import remove, rmdir, walk, mkdir
from shutil import copy2, rmtree, copytree

check = "nv_dispi.inf_amd64_"
syspath = "C:/Windows/System32/"
sharepath = "//Quantum7/Share/Cuda_Drivers/" # Edit to path of Share drive
folders = []
direc = []
dlls = []
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

def diff(li1, li2): 
    return list(set(li1)-set(li2))+list(set(li2)-set(li1))

# What directory exists in 
for (dirpath, dirnames, filenames) in walk(syspath+'HostDriverStore/FileRepository/'):
    direc.extend(dirnames)
    nvidiafilepres = [i for i in direc if i.startswith(check)]
existing = nvidiafilepres.pop()

# Get a list current files and directory's in Share drive:
for (dirpath, dirnames, filenames) in walk(sharepath):
    dlls.extend(filenames)
    folders.extend(dirnames)
    nvidiafile = [i for i in folders if i.startswith(check)]
file = nvidiafile.pop()

# Removing the existing folder if not the same as in sharepath:
if file != existing: [rmtree(syspath+'HostDriverStore')]
else: [print("Already Updated - Nothing to do.")] [exit(0)]

# Compare available files with required:
if (diff(dlls, needed_dlls)) == [ ]: [print('Deleting old Nvidia DLL files in System32...')]
else:
    needed = (diff(dlls, needed_dlls))
    print("ERROR: following is needed in "+sharepath+" for successful install: ")
    for i in needed: [print(i + "\r")] [exit(1)]

# Try to delete old Nvidia DLL files in System32:
for i in needed_dlls:
    remove(syspath+i)
    copy2(str(sharepath+i), str(syspath)) # Copy new Nvidia DLL files from Share drive
print("Copied new Nvidia DLL files from: "+sharepath)
copytree(str(sharepath+file), str(syspath+"HostDriverStore/FileRepository/"+file))
print("Completed.") [exit(0)]
