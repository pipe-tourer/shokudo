import psycopg2

conn = psycopg2.connect(
    host='localhost',
    dbname='team6db',
    user='team6',
    password='9RgBGqgc')

cur = conn.cursor()

cur.execute('')

cur.close()
conn.close()
