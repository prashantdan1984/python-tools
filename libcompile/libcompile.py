import os
import sys

arg = sys.argv

def ex():
    pass

if "-f" in arg:
    try:
        file = arg[arg.index("-f")+1]
        f1 = open(file,"r")
        f2 = open(file.replace(".py",".pyx"),"w+")
        f2.write(f1.read())
        f2.close()
        f1.close()
        f3 = open("setup.py","w+")
        f3.write("""
from distutils.core import setup
from Cython.Build import cythonize

setup(
     ext_modules = cythonize("{}.pyx")
)""".format(file.replace(".py","")))
        f3.close()
        if "-i"in arg:
            os.system("python setup.py build_ext --inplace")
            os.system("cp {}.cp35-win_amd64.pyd C:\\Python35\\Lib\\site-packages\\".format(file.replace(".py","")))
            os.system("del {}.cp35-win_amd64.pyd".format(file.replace(".py","")))
            os.system("del {}.c".format(file.replace(".py","")))
            os.system("del {}.pyx".format(file.replace(".py","")))
        elif "--indir" in arg:
            try:
                path = arg[arg.index("--indir")+1]
                os.system("python setup.py build_ext --inplace")
                try:
                    os.system("del {}\\{}.cp35-win_amd64.pyd".format(path,file.replace(".py","")))
                except:
                    pass
                os.system("cp {}.cp35-win_amd64.pyd {}".format(file.replace(".py",""),path))
                os.system("del {}.cp35-win_amd64.pyd".format(file.replace(".py","")))
                os.system("del {}.c".format(file.replace(".py","")))
                os.system("del {}.pyx".format(file.replace(".py","")))
            except:
                print ("Please specify a path")        
        else:
            os.system("python setup.py build_ext --inplace")
    except:
        print ("Please choose file")     
   
elif "-h" in arg:
    print ("-f filename")
    print ("-i to install in python\'s directory")
    print ("--indir path to install in specific path")

else:
    print ('Please Select File')
