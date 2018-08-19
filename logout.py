#!usr/bin/python
import subprocess

subprocess.call(["shutdown", "-f", "-s", "-t", "60"])
print "Logout in less than 1 min."
