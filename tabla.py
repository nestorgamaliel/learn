import sqlite3

con = sqlite3.connect('python.db')
cur = con.cursor()
sql = """create table pyversions (
	branch text primary key,
	release_at_year integer,
	release_at_month integer,
	release_manager text
	)"""

cur.execute(sql)
