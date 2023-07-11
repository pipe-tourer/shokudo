import psycopg2

def fetch_dailymenu(type, dte):
    
    conn = psycopg2.connect(
        host='localhost',
        dbname='team6db',
        user='team6',
        password='9RgBGqgc')
    
    cur = conn.cursor()
    
    if  type = 'A': #A/B選択情報による分岐
        cur.execute('select * from dailymenu_a where hiduke = %s', [dte])  #選択した日付情報
    else:
        cur.execute('select * from dailymenu_b where hiduke = %s', [dte])  #選択した日付情報
    
    row = cur.fetchall()    #rowにメニュー情報がリストで入る
    #print(row)
    
    cur.close()
    conn.close()
    
    return row
