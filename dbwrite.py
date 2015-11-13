__author__ = 'meerapatil'
import _mysql
import sys

file = open("jobscloud.txt", "w")




try:
    con = _mysql.connect('localhost', '', '', 'testdb')
    query = "SELECT * FROM jota INTO OUTFILE \'/Users/meerapatil/jobscloud.txt\';"
    con.query(query)



except _mysql.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    pass

finally:
    if con:
        con.close()


file.close()
