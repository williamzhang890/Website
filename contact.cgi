#!/usr/bin/python3
import cgi
import cgitb; cgitb.enable()
import time
print ("Content-Type: text/html\n\n")

import smtplib
from email.mime.text import MIMEText
import os

form = cgi.FieldStorage()
msg = form['msg'].value
first = form['firstName'].value
last = form['lastName'].value
sender = form['email'].value

t = time.localtime()
time_str = '{}-{}-{}_{}-{}_{}'.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

path = './mail/{}_{}_{}.mail'.format(first, last, time_str)

with open(path, 'w') as f:
    f.write("From: {} {} <{}>\n".format(first, last, sender))
    f.write(msg)

header = "From: {} {} <{}> at {}\n".format(first, last, sender, time_str)

status_msg = 'Failed to send message.'
try:
    os.system('mail wtzhang23@gmail.com < {}'.format(path))
    status_msg = 'Succeeded sending'
except:
    pass
page = '''
<html>
    <head>
        <title>Contact Me</title>
        <meta name = "description" content = "Submitted Form"/>
        <meta http-equiv = "author" content = "William Zhang"/>
        <meta http-equiv="refresh" content="3;url=contact.html"/> 
        <link href = "styles.css" type = "text/css" rel = "stylesheet"/>
        <header>
            <div class = "center">
                <div class = "navigator">
                    <h1>Hi. I'm William Zhang.</h1>
                    <table>
                        <tr>
                            <td>
                                <a href="index.html">Home</a>
                            </td> 
                            <td>
                                <a href="projects.html">Projects</a>
                            </td>
                            <td>
                                <a href = "resume.html">Resume</a>
                            </td>
                            <td>
                                <a href= "contact.html">Contact Me</a>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
        </header>
    </head>
    
    <body>
        <div class = "center">
            <div class = "page">
                <b> {} You should be redirected soon.
            </div>
        </div>
    </body>
</html>
'''.format(status_msg)
print(page)