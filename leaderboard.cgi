#!/usr/bin/python3
import cgi
import cgitb; cgitb.enable()
import os
from validate_email import validate_email

print ("Content-Type: text/html\n\n")
page = '''
<html>
    <head>
        <title>Leaderboard</title>
        <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Expires" content="0">
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
                <h1>
                    Leaderboard.
                </h1>
                <div class="row">
                    <div class = "column">
                        <form id="form" action="leaderboard.cgi" method="post">
                            <fieldset>
                                <legend>Upload your results</legend>
                                <div class="row">
                                    {}
                                </div>
                                <div class="row">
                                    <div class="column">
                                        <div>
                                            <label for="username" size=80>UTCS id:</label>
                                        </div>
                                    </div>
                                    <div class="column">
                                        <div>
                                            <input type="text" id="username" name="username" required="required" style="width:100%;"/>
                                        </div>
                                    </div>
                                </div>
                                <div class="row">
                                    <div>
                                        <input type="file" name="fileToUpload" id="fileToUpload">
                                    </div>
                                </div>
                                <div class="row">
                                        <input type="submit" value="Submit" style="flex-grow:0;">
                                </div>
                                <input type="hidden" id="submitted" name='submitted' value='1'>     
                            </fieldset>
                        </form>
                    </div>
                    <div class="column" style="flex-grow:3;">
                    </div>
                </div>
            </div>
        </div>
    </body>
</html>
'''

# code copied from http://homepages.math.uic.edu/~jan/mcs275/mcs275notes/lec35.html
form = cgi.FieldStorage()
submitted, username, f = form.getvalue('submitted'), form.getvalue('username'), form.getvalue('file')
email = username + "@cs.utexas.edu"
form_msg = ''

if submitted == '1':
    if validate_email (email):  
        if not os.path.isdir(username):
            os.mkdir(username)
        saved_filepath = os.path.join("leaderboard", username, "submission")
        template = os.path.join("leaderboard", "confirmation_email")
        new_confirmation_addr = os.path.join("leaderboard", username, "email")
        id_addr = os.path.join("leaderboard", username, "id")
        i = os.urandom(32)
        with open(saved_filepath, 'a') as w:
            w.write(f)
        
        with open(template, 'r') as r:
            s = r.readlines()
            with open(new_confirmation_addr, 'a') as w:
                w.write(s.format(i))
            with open(id_addr, 'a') as w:
                w.write(id_addr)
            

        os.system('mail {} < {}'.format(username + '@cs.utexas.edu', new_confirmation_addr))

    else:
        form_msg = 'Invalid Email.'
print(page.format(form_msg))