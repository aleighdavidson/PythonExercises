import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
# Added "Documents" as there are no files, only directories in my home directory
pattern = os.path.join(hdir, "Documents", '*')

# TODO: Use the glob.glob() function to obtain the list of filenames
hdirFiles = glob.glob(pattern)
print(hdirFiles)
# TODO: use os.path.getsize to find each file's size
for e in hdirFiles:
    print(e + "  Size (bytes): " + str(os.path.getsize(e)))
# TODO: Add a test to only display files that are not zero length
for e in hdirFiles:
    if os.path.getsize(e) != 0:
        print(e + "  Size (bytes): " + str(os.path.getsize(e)))
    else:
        continue
# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
for e in hdirFiles:
    if os.path.getsize(e) != 0:
        print(os.path.basename(e) + "  Size (bytes): " + str(os.path.getsize(e)))
    else:
        continue