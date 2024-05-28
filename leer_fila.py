import sqlite3

con = sqlite3.connect('python.db')
cur = con.cursor()
res = cur.execute('select * from pyversions') 
fila = res.fetchone()
print(fila)
print('---')
for fila in res:
	print(fila)
