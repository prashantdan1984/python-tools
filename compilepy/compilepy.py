import os
import sys

arg = sys.argv

if "-f" in arg:
    file = arg[arg.index("-f")+1]
    if "--indir" in arg:
        try:
            path = arg[arg.index("--indir")+1]
            os.system("pyinstaller {}".format(file))
            os.system("cp dist\\{} {}".format(file.replace(".py",""),path))
            print("Compiled successfully")
        except:
            print ("please enter path")
            
    elif "--i":
        os.system("pyinstaller {}".format(file))
        os.system("cp dist\\{} C:\\bin".format(file.replace(".py","")))
        print("Compiled successfully")
    else:
        pass           
elif "-h" in arg or "-help" in arg:
    print ("-f filename")
    print ("--indir path")
    print ("-i for system path")
else:
    print ("Please Select File to Compile")
