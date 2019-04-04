#! /usr/bin/env python3

import cgi
import cgitb
import private_passwords as PP

cgitb.enable(display=0, logdir="/var/log/httpd/cgi_err/")

host=PP.DB_HOST
user=PP.DB_USER
password=PP.DB_PASSWORD
db=PP.DB_DATABASE
def write_html():
        form = cgi.FieldStorage()
        id = int(form["id"].value)
        print("""<html>
<body>

<h2>New Comment Form</h2>

<form action="process__comment.py" method="post">
  User name:<br>
  <input type="text" name="userName" value="commentName">
  <br>
  Comment to be made:<br>
  <input type="text" name="postString" value="add your comment here">
  <br> <br>
  ID:(Do not edit!) <br>
  <input type="text" name="id" value=%s>
 <br><br>
 <input type="submit" value="Create">
</form>

<p>If you click the "Create" button, the comment will be added to our webpage.</p>

</body>
</html>
""" % id, end="")





#The below runs each time we are called.
try:
        print("Content-type: text/html")
        print()

        write_html()
except FormError as e:
        print(""" <html>
<head><titlte> 346 - Brendan Project 2</title></head>
<body>
<p> ERROR: %s
</p><a href="application.py">Return to thread list</a>
</body>
""", end="")
