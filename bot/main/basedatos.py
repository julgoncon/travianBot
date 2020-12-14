import sqlite3

def createdatabase():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    #cursor.execute("CREATE TABLE asignaciones(id integer PRIMARY KEY AUTOINCREMENT, cuenta text, pais text,ip text )")
    cuenta='mockingjay'
    cursor.execute("INSERT INTO asignaciones(id,cuenta,pais,ip) VALUES (1,'"+cuenta+"','Portugal','111.111.111.111')")
    con.commit()
    con.close()

def getCoste(level,i):
    con = sqlite3.connect('edificios.db')
    cursor = con.cursor()
    if i==0 or i==2 or i==13 or i==16:
        cursor.execute("SELECT madera,barro,hierro,cereal FROM leñador WHERE id=="+str(level+1)+"")
    if i==3 or i==6 or i==9 or i==10:
        cursor.execute("SELECT madera,barro,hierro,cereal FROM hierro WHERE id=="+str(level+1)+"")
    if i==4 or i==5 or i==15 or i==17:
        cursor.execute("SELECT madera,barro,hierro,cereal FROM barrera WHERE id=="+str(level+1)+"")
    if i==7 or i==8 or i==11 or i==12 or i==1 or i==14:
        cursor.execute("SELECT madera,barro,hierro,cereal FROM cereal WHERE id=="+str(level+1)+"")
    coste=cursor.fetchall()
    return coste[0]

