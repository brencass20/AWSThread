#! /usr/bin/env python3
import cgi
import cgitb
import MySQLdb
import private_passwords

host=PP.DB_HOST
user=PP.DB_USER
password=PP.DB_PASSWORD
db=PP.DB_DATABASE

form = cgi.FieldStorage()
id= form["id"].value
#id=-1
conn=MySQLdb.connect(host=host,user=user,passwd=password,db=db)
cursor=conn.cursor()
sql ="""UPDATE threads SET threadLikes = threadLikes + 1 WHERE threadId=%s""" % id
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
print ('<a href="application.py">Return to homepage</a>')
print ('</body>')
print ('</html>')
