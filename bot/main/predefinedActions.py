import sqlite3
import seleniumFunct as sf
import random
import vpn_settings as vpn
import time

def cambiarVPNLogin(cuenta):
    vpn.connectVPN(cuenta)
    sf.login(cuenta)
    

def subirPorDefecto():
    start_time=time.time()
    while(True):
        lista=sf.casillasASubir()
        sf.subirRecursos(lista,start_time)
        current_time=time.time()
        if current_time-start_time>=100:
            print(current_time-start_time)
            return print('CAMBIO: han pasado 7 min')





