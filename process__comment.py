#! /usr/bin/env python3
import cgi
import cgitb
import time
import MySQLdb
import random
import private_passwords as PP
host=PP.DB_HOST
user=PP.DB_USER
passwrd=PP.DB_PASSWORD
db=PP.DB_DATABASE

form = cgi.FieldStorage()
userName = form["userName"].value
postString = form["postString"].value
threadID = form["id"].value
commentID = random.randint(1,10000)

conn=MySQLdb.connect(host=host,user=user,passwd=passwrd,db=db)
cursor=conn.cursor()
sql = """INSERT INTO comments (threadId,commentID, commentContent, commentAuthor, commentLikes) VALUES (%s,%s,%s, %s, %s)"""
val = (threadID, commentID, postString, userName, 0)
cursor.execute(sql, val)
conn.commit()
cursor.close()
conn.close()

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h4>Comment Success!</h4>')
print ('<a href="comment.py?id=%s">Return to thread</a>'% threadID)
print ('</body>')
print ('</html>')
