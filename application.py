#! /usr/bin/env python3

#Much of this file is adapted from list.py provided by Russ Lewis on
# https://github.com/russ-lewis/ttt_-_python_cgi/list.py

import cgi

#Enable debugging.  Python docs recommend for testing. Should not be left enabled.
#import cgitb
#cgit.enable(display=0, logdir="/var/log/httpd/cgi_err/")

import MySQLdb
import private_passwords as PP

#The following function handles the processing of the actual test of the HTML File.
#It writes everything from the HTML header to the content to the closing tabs at the bottom.
host=PP.DB_HOST
user=PP.DB_USER
password=PP.DB_PASSWORD
db=PP.DB_DATABASE
def wrtie_html():
        # See https://docs.python.org/3.4/library/cgi.html
        form = cgi.FieldStorage()

        print("""<html>
<head><title> Brendan and Corey PostThread Project 2</title></head>
<body>

<h2> Brendan and Corey PostThread - Project 2</h2>
""", end="")
        print("""<p>
<font size="+1"><b>This is a simple feed that allows users to post threads, comment on these threads, and like those threads they like the most.  Those with the most likes will be ordered to the top of the thread.</b></font>
""", end="")
        write_create_thread_form()

        #Call DB and iterate through threads and comments.
        conn=MySQLdb.connect(host=host,user=user,passwd=password,db=db)
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM threads WHERE threadId IS NOT NULL;")
        allposts=[]
        for row in cursor.fetchall():
                id = int(row[0])
                post = row[1]
                author = row[2]
                likes = int(row[3])

                allposts.append({"id":id, "post":post, "author":author, "likes":likes})
        cursor.close()

        write_posts(allposts)
        print("""</body></html>""", end="")


def write_create_thread_form():
        print("""<p><b> Create new thread</b>

<form action="create_thread.py" method="post">
<input type=submit value="Create">
</form>

""", end="")


def write_posts(allposts):
        print("""<p>
<font size="+1"><b> POSTS </b></font>
        <br><table border = 1>
                <tr> <td><b>Likes</b></td> <td><b>Message</b></td> <td><b>Author</b></td> <td><b>Comment</b></td> <td><b>Upvote</b></td> </tr>""", end="")

        for p in allposts:
                id = p["id"]
                post=p["post"]
                author=p["author"]
                likes=p["likes"]
                mark = "</b></font>"
                totStr= """     <td>%s%d</td> <td>%s</td>  <td>%s</td> <td><a href="comment.py?id=%d">%s</a></td>""" % (mark, likes, post, author, id, author)

                #form action for each button
                print("""
                <tr>
                %s <td><a href="upvotethread.py?id=%s">Upvote</a>
                </tr>""" % (totStr, id), end="")
        print("""       </table>

""", end="")


print("Content-Type: text/html;charset=utf-8")
print()
wrtie_html()

    # see https://docs.python.org/3.4/library/cgi.html for the basic usage
    # here.
