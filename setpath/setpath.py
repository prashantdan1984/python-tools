import os
import sys

arg = sys.argv

if len(arg)>1:
    os.popen("setx path \"%path%;{}\" /M".format(arg[1]))
else:
    print ('Please Enter Path')
    
