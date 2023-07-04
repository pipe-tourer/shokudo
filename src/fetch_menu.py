import psycopg2
import datetime

def fetch_menu(selected_menuname):
    
    conn = psycopg2.connect(
        host='localhost',
        dbname='team6db',
        user='team6',
        password='9RgBGqgc')
    
    cur = conn.cursor()
    
    cur.execute('select * from menu where menu_name = %s', [selected_menuname])  #選択されたメニュー名
    row = cur.fetchall()    #rowにメニュー情報がリストで入る
    print(row)
    
    cur.close()
    conn.close()
