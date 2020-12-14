import os
import seleniumFunct as sf
import time
import sqlite3
import sys


#os.system('powershell.exe Add-VpnConnection -Name "vpnRusia2" -ServerAddress "rus1.freevpn4you.net"')

#print('vieja ip: '+ sf.public_ip())
#os.system('powershell.exe Add-VpnConnection -Name "vpn2" -ServerAddress "swe1.freevpn4you.net"')
def connectVPN(cuenta):
    if cuenta=='unicornioazul':
        pais="Portugal"
    if cuenta=='gothem':
        pais="France"
    if cuenta=="swishbish":
        pais="Switzerland"


    old_ip=sf.public_ip()
    os.system('cd C:\Program Files (x86) & cd NordVPN & nordvpn -c -g '+pais+'')
    time.sleep(20)
    new_ip=sf.public_ip()
    while(old_ip==new_ip):
        old_ip=sf.public_ip()
        os.system('cd C:\Program Files (x86) & cd NordVPN & nordvpn -c -g '+pais+'')
        time.sleep(20)
        new_ip=sf.public_ip()


    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    cursor.execute("SELECT ip FROM asignaciones WHERE ip=='"+new_ip+"'")
    ips=cursor.fetchall()
    if len(ips) !=0:
        cursor.execute("SELECT ip FROM asignaciones WHERE ip=='"+new_ip+"' AND pais!='"+pais+"'")
        ipsPais=cursor.fetchall()
        if len(ipsPais) !=0:
            sys.exit()
        pass
    else:
        cursor.execute("INSERT INTO asignaciones(cuenta,pais,ip) VALUES('"+cuenta+"','"+pais+"','"+new_ip+"')")       
        con.commit()
        cursor.execute("SELECT * FROM asignaciones")
        x=cursor.fetchall()
        print(x)
        con.close()
    
#print('nueva ip: '+ sf.public_ip())