#!/usr/bin/python
print "\t\t\t*--------------------------------------------*"
print "Welcome"
print "Press 1 to check current date and time"
print "Press 2 to check RAM and CPU status"
print "Press 3 to open default web browser of your current OS"
print "Press 4 to open webcam"
print "Press 5 to reboot your system"
print "Press 6 to search something on google"
print "Press 7 to scan all MAC addresses of your current network"
print "Press 8 to seach something on google and list top 5 URL from search result"
print "Press 9 to logout from your current OS"
print "Press 10 to Exit"

# taking input from user

choice = input()
if (choice == 1):
    execfile ('date_time.py')
    print "\n"
else:
    if(choice == 2):
        pass
    else:
        if(choice == 3):
            pass
        else:
            if(choice == 4):
                execfile ('webcam.py')
                print "\n"
            else:
                if(choice == 5):
                    pass
                else:
                    if(choice == 6):
                        execfile ('search_google.py')
                        print "\n"
                    else:
                        if(choice == 7):
                            pass
                        else:
                            if(choice == 8):
                                pass
                            else:
                                if(choice == 9):
                                    pass
                                else:
                                    if(choice == 10):
                                        print "Exit"
                                    else:
                                        print "Invalid Input ...."
                                        time.sleep(2)
                                        execfile ('menu.py')


