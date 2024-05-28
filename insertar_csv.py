import sqlite3

con = sqlite3.connect('python.db')
cur = con.cursor()


f = open('pyversions.csv')
fields = f.readline().strip().split(',')
print(fields)
data = [{f: v for f, v in zip(fields, line.strip().split(','))} for line in f]
sql = 'insert into pyversions values (:branch, :year, :month, :manager)'

print(data)

cur.executemany(sql, data)
con.commit()
