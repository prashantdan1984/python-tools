import os
import sys

arg = sys.argv

if len(arg)>1:
    os.system("xcopy {} {} /O/H/K/E/X".format(arg[1],arg[2]))
else:
    print ("Please Select File to copy")
