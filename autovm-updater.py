from os import remove, walk, mkdir
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

def diff(li1, li2):
    return list(set(li1)-set(li2))+list(set(li2)-set(li1))

# Get a list current files and directory's in Share drive:
for (dirpath, dirnames, filenames) in walk(sharepath):
    dlls.extend(filenames)
    folders.extend(dirnames)
    nvidiafile = [i for i in folders if i.startswith(check)]
    break

# Compare available files with required:
if (diff(dlls, needed_dlls)) == [ ]:
    print('Deleting old Nvidia DLL files in System32...')
else:
    needed = (diff(dlls, needed_dlls))
    print("ERROR: following is needed in "+sharepath+" for successful install: ")
    for i in needed:
        print(i + "\r")
    exit(1)

# Try to delete old Nvidia DLL files in System32 and removing Driver file:
for i in needed_dlls:
    try:
        remove(syspath+i)
        rmtree(str(syspath)+'HostDriverStore')
    except:
        continue
print("Copy new Nvidia DLL files from: "+sharepath)

# Copy new Nvidia DLL files from Share drive:
for i in needed_dlls:
    copy2(str(sharepath+i), str(syspath))
print("Copying files from: "+sharepath)

if nvidiafile == [ ]:
    print("ERROR: Could not find: "+check+"000000... in "+sharepath)
    exit(1)
else:
    file = nvidiafile.pop()
    copytree(str(sharepath+file), str(syspath+"HostDriverStore/FileRepository/"+file))
print("Completed.")
exit(0)
