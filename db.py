import sqlite3
con = sqlite3.connect('//django//mysite//db.sqlite3')
cur = con.cursor()
for row in cur.execute('SELECT * FROM UserDetail'):
    print(row)