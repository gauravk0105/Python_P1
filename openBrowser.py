#!usr/bin/python
import os
import sys

url = 'https://google.com'
print "trying to open default web browser...... "
if sys.platform=='win32':
    os.startfile(url)
elif sys.platform=='darwin':
    subprocess.Popen(['open', url])
else:
    try:
        subprocess.Popen(['xdg-open', url])
    except OSError:
        print 'Please open a browser on: '+url

execfile ('menu.py')
