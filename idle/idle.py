
import sys
import os

get = sys.argv

if len(get)>1:
        file = get[1]
        #print (file)
        string = "C:\Python35\pythonw.exe \"C:\Python35\Lib\idlelib\idle.pyw\" {}".format(file)
        #print (string)
        os.popen(string)
else:
	os.popen("C:\Python35\pythonw.exe \"C:\Python35\Lib\idlelib\idle.pyw\"")
	


