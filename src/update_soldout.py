import psycopg2

def update_soldout(selected_id):
    
    conn = psycopg2.connect(
        host='localhost',
        dbname='team6db',
        user='team6',
        password='9RgBGqgc')
    
    cur = conn.cursor()
    
    
    # = .get('')
    #test_id = input()
    #select_id = test_id
    
    #cur.execute('select * from soldout')
    #test1 = cur.fetchall()
    #print(test1)
    
    cur.execute("""
update soldout set soldout = case
when soldout = true then false
else true
end where cast(menu_id as integer) = %s;
""", [selected_id])
    
    
    #cur.execute('update soldout set soldout = false where soldout = true and cast(menu_id as integer) = %s', [select_id])
    #cur.execute('update soldout set soldout = true where soldout = not true and cast(menu_id as integer) = %s', [select_id])   #変更するmemu_id
    #cur.execute('update soldout set soldout = false where soldout = true and cast(menu_id as integer) = %s', [select_id])
    #cur.execute('update soldout set soldout = true where cast(menu_id as integer) = %s', [select_id])
    #cur.execute('update soldout set soldout = true where soldout = false')
    
    conn.commit()
    
    #cur.execute('select * from soldout')
    #test2 = cur.fetchall()
    #print(test2)
    
    cur.close()
    conn.close()
    

