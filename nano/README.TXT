Nano for Win32 README
---------------------

This version of nano for Win32 systems was compiled using the
standard nano source with a few tweaks (soon to be merged into the
official nano distribution, hopefully), cygwin and PDCurses 2.4.  

INSTALL
-------
	- Copy cygwin1.dll somewhere where Windows will be able to see it (C:\WINNT or 
	  C:\WINNT\SYSTEM32 is good for NT users and C:\WINDOWS or C:\WINDOWS\SYSTEM 
	  are good for WIn9x users.  You can always leave it in the same directory as the
	  nano executable if you're really lazy.
	- Put the nano.exe executable somehwere useful (your desktop or C:\WINDOWS perhaps)
	- Have fun with it.

COMPILATION
-----------
This is how I compiled this binary, if you're at all interested:
First I downloaded and installed up cygwin, a great FREE product I can't recommend
highly enough for those who must use Windows (http://sources.redhat.com/cygwin).

Then I obtained PDCurses from 
http://dv.go.dlr.de/fresh/unix/src/contrib/.warix/PDCurses-2.4.tar.gz.html

I compiled PDCurses something like this:

$ tar xvfz PDCurses-2.4.tar.gz
$ mv PDCurses-2.4 /usr/local/pdcurses
$ cd /usr/local/pdcurses
$ cp win32/gccwin32.mak Makefile
$ vi Makefile 
$ make
$ ln -sf pdcurses.a libcurses.a

And finally 
$ export CFLAGS="-O2 -Wall -I/usr/local/pdcurses"
$ export LDFLAGS="-L/usr/local/pdcurses"

(RE)DISTRIBUTION
------------
Please see the LICENSE.TXT file for terms of distribution for these files.

BUGS
----
If you'be got them, send them my way.
	
Win95 users may have to upgrade to at least IE4 or 5 to gat this binary to work, or
it may not work at all.  I have tested it under NT and 98 and its....usable, I guess.
Patches and feedback welcome.

Chris Allegretta, chrisa@asty.org