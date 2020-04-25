#!/usr/bin/python3
import cgi
import cgitb; cgitb.enable()
import time
print ("Content-Type: text/html\n\n")

import smtplib
from email.mime.text import MIMEText

form = cgi.FieldStorage()
msg = form['msg'].value
first = form['firstName'].value
last = form['lastName'].value
sender = form['email'].value

t = time.localtime()
time_str = '{}-{}-{}_{}-{}_{}'.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)

with open('./mail/{}_{}_{}.mail'.format(first, last, time_str), 'w') as f:
    f.write("From: {} {} <{}>\n".format(first, last, sender))
    f.write(msg)

page = '''
<html>
    <head>
        <title>Contact Me</title>
        <meta name = "description" content = "Submitted Form"/>
        <meta http-equiv = "author" content = "William Zhang"/>
        <meta http-equiv="refresh" content="0;url=contact.html"/> 
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
                <b> Your message was sent. You should be redirected soon.
            </div>
        </div>
    </body>
</html>
'''
print(page)