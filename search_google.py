#!usr/bin/python
import webbrowser

print "To Search Something on Google"
query = raw_input("Enter Query : ")
flag = webbrowser.open('https://www.google.co.in/#q='+query)
if not(flag) :
    print "Error : Unable To Open"
    print "Plz wait.... redirecting to menus"
    time.sleep(2)
    execfile ('menu.py')
print "collecting......"
execfile ('menu.py')
