import psycopg2
import datetime

def send_dailymenu(dte):
    
    conn = psycopg2.connect(
        host='localhost',
        dbname='team6db',
        user='team6',
        password='9RgBGqgc')
    
    cur = conn.cursor()
    
    #str = '20230624'
    #dte = datetime.datetime.strptime(str, '%Y%m%d')
    
    cur.execute('select * from dailymenu_a where menu_date = %s', [dte])  #今日の日付の変数
    row_a = cur.fetchall()  #rowにメニュー情報がリストで入る
    cur.execute('select * from dailymenu_b where menu_date = %s', [dte])  #今日の日付の変数
    row_b = cur.fetchall()  #rowにメニュー情報がリストで入る
    
    #print(row_a)
    
    cur.close()
    conn.close()
    
    retrun row_a, row_b
