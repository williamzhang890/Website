#!/usr/bin/python
import subprocess
import time
import cgi
import os
import cgitb; cgitb.enable()

print ("Content-Type: text/html\n\n")
print ("<html>")
print ("<head>")
print ("<title>Leaderboard</title>")
print ("</head>")
print ("<body>")



print ("</body>")
print ("</html>")


def runTests():
    start = time.time()
    cmd = 'make clean test'
    subprocess.call(cmd, shell = True)
    stop = time.time()
    print(stop - start)


