#! /usr/bin/env python3

import cgi
import cgitb
cgitb.enable(display=0, logdir="/var/log/httpd/cgi_err/")

def write_html():
        form = cgi.FieldStorage()
        print("""<html>
<body>

<h2>New Thread Form</h2>

<form action="process_form.py" method="post">
  User name:<br>
  <input type="text" name="userName" value="addName">
  <br>
  Post to be made:<br>
  <input type="text" name="postString" value="add your thread here">
  <br>
  <input type="submit" value="Create">
</form>

<p>If you click the "Create" button, the thread will be added to our webpage.</p>

</body>
</html>
""", end="")






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
</html> """ % e.msg, end = "")
