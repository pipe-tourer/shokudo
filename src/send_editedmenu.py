import psycopg2

def send_editedmenu(,,,,):
    conn = psycopg2.connect(
        host='localhost',
        dbname='team6db',
        user='team6',
        password='9RgBGqgc')
    
    cur = conn.cursor()
    
    
    cur.execute('update menu set (menu_name, energy, protein, lipid, carbohydrates, salt, wheat, egg, milk, buckwheat, peanut, shrimp, crab)\
 = (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ',(,,,,,,,,,,,,,,,,,,)) #それぞれの変数入れとく
    
    cur.close()
    conn.close()

