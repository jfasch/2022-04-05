import sys
import sqlite3
import pprint
import csv


sqlfilename = sys.argv[1]
csvfilename = sys.argv[2]

connection = sqlite3.connect(sqlfilename)
csvfile = open(csvfilename, 'w')



cursor = connection.cursor()

resultset = cursor.execute('select * from users;')

userdb = {}

for svnr, firstname, lastname in resultset:
    userdb[svnr] = (firstname, lastname)

# pprint.pprint(userdb, indent=4)

csv_writer = csv.writer(csvfile, delimiter=';', quotechar='"')

csv_writer.writerow(['SVNr.', 'Firstname', 'Lastname'])
for svnr, (firstname, lastname) in userdb.items():
    csv_writer.writerow([svnr, firstname, lastname])
    
