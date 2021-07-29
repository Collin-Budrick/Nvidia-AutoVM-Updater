from os import walk
from shutil import copy2, rmtree, copytree

check = "nv_dispi.inf_amd64_"
syspath = "C:/Windows/System32/"
sharepath = "//Quantum7/Share/Cuda_Drivers/" # Edit to path of Share drive
folders = []
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

# Get nv_dispi.inf_amd64_* in FileRepository:
for (dirpath, dirnames, filenames) in walk(str(syspath+"DriverStore/FileRepository")):
    folders.extend(dirnames)
    nvidiafile = [i for i in folders if i.startswith(check)]
    break
file = nvidiafile.pop()

# Delete old files in Share drive:
while True:
    try:
        rmtree(str(sharepath))
    except:
        break
print("Deleted old files & folders in: "+sharepath)
copytree(str(syspath+"DriverStore/FileRepository/"+file), str(sharepath+file))
print("Copied: "+file+" to "+sharepath)

# Get a list current files and directory's in System32:
for (dirpath, dirnames, filenames) in walk(syspath):
    dlls.extend(filenames)
    folders.extend(dirnames)
    break

# Get New Nvidia folder and files from System32:
for i in needed_dlls:
    copy2(str(syspath+i), str(sharepath))
print("Copied Updated: Dll's to "+sharepath+" from "+syspath+"\nCompleted.")
exit(0)
