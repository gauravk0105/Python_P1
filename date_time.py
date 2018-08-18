#!usr/bin/python

#import time module
import time

localtime = time.asctime(time.localtime(time.time()))
tlst = localtime.split(" ")
print "Current Date :",tlst[0],tlst[2],tlst[1],tlst[-1]
print "Current Time :",tlst[3]
print "Plz Wait..... returning to menus"
time.sleep(2)
execfile ('menu.py')
