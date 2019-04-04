#! /usr/bin/env python3
import cgi
import cgitb
import MySQLdb
import private_passwords as PP


host=PP.DB_HOST
user=PP.DB_USER
password=PP.DB_PASSWORD
db=PP.DB_DATABASE

form = cgi.FieldStorage()
id= form["id"].value
idT=form["idT"].value
conn=MySQLdb.connect(host=host,user=user,passwd=password,db=db)
cursor=conn.cursor()
sql ="""UPDATE comments  SET commentLikes = commentLikes + 1 WHERE commentID=%s""" % id
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h4>Upvote Success!</h4>')
print ('<a href="comment.py?id=%s">Return to homepage</a>'% idT)
print ('</body>')
print ('</html>')
