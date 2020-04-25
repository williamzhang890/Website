#!/usr/bin/python3
import cgi
import cgitb; cgitb.enable()
from smtplib import SMTP
from getpass import getpass

print ("Content-Type: text/html\n\n")
page = '''
<html>
    <head>
        <title>Contact Me</title>
        <meta name = "description" content = "Leaderboard"/>
        <meta http-equiv = "author" content = "William Zhang"/>
        <link href = "styles.css" type = "text/css" rel = "stylesheet"/>
        <header>
            <div class = "center">
                <div class = "navigator">
                    <div class = "center">
                        <div class="row">
                            <h1>Hi. I'm William Zhang.</h1>
                        </div>
                        <div class="row">
                            <div>
                                <a href="index.html">Home</a>
                            </div>
                            <div>
                                <a href="projects.html">Projects</a>
                            </div>
                            <div>
                                <a href = "resume.html">Resume</a>
                            </div>
                            <div>
                                <a href= "contact.html">Contact Me</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </header>
    </head>
    
    <body>
        <div class="center">
            <div class="page">
                <div class="row">
                    <form id="form" action="leaderboard.cgi" method="post">
                        <fieldset>
                            <legend>Upload your results</legend>
                            <div class="row">
                                <div class="column">
                                    <div>
                                        <label for="username" size = 80>User Name:</label>
                                    </div>
                                    <div>
                                        <label for="password" size = 80>Password:</label>
                                    </div>
                                </div>
                                <div class="column">
                                    <div>
                                        <input type="text" id="username" name="username" required="required" size=20/>
                                    </div>
                                    <div>
                                        <input type="password" id="password" name="password" required="required" size=20/>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div>
                                    <input type="file" name="fileToUpload" id="fileToUpload">
                                </div>
                            </div>
                            <div class="row">
                                    <input type="submit" value="Submit">
                            </div>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div>
    </body>
</html>
'''
print(page)

'''
# code copied from http://homepages.math.uic.edu/~jan/mcs275/mcs275notes/lec35.html
connected = False
try:
    s = SMTP('mail2.cs.utexas.edu', 587)
    s.starttls()
    connected = True
except:
    print('Failed to connect to server.')

if connected:
    #user = input("UTCS username: ")
    #password = getpass("UTCS password: ")
    form = cgi.FieldStorage(environ="post")
    user, password = input(), getpass()
    success = False
    for _ in range(3): # three attempts to log in
        try:
            result = s.login('{}@cs.utexas.edu'.format(user),password)
            success = True
            break
        except:
            pass

        try:
            result = s.login(user, password)
            success = True
            break
        except:
            pass
    if success:
        pass
    else:
        print('Failed to login.')
'''