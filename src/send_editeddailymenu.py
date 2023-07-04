import psycopg2
import datetime

conn = psycopg2.connect(
    host='localhost',
    dbname='team6db',
    user='team6',
    password='9RgBGqgc')

cur = conn.cursor()

#test_list = (datetime.date(2023, 6, 24), 'testmn2', 13.6, 23.4, 56.5,)

#if  = : #A/B選択情報による分岐
    cur.execute('update dailymenu_a set (menu_name, energy, protein, lipid, carbohydrates, salt, wheat, egg, milk, buckwheat, peanut, shrimp, crab)\
     = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(,,,,,,,,,,,,,,,,,,))  #それぞれの変数入れとく
#else:
#    cur.execute('update dailymenu_b set (menu_name, energy, protein, lipid, carbohydrates, salt, wheat, egg, milk, buckwheat, peanut, shrimp, crab)\
#     = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',(,,,,,,,,,,,,,,,,,,))  #それぞれの変数入れとく

cur.close()
conn.close()
