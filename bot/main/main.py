import seleniumFunct as sf
import os
import vpn_settings as vpn
import predefinedActions as pa
import telegram as tl
"""
cuenta=input('cuenta: ')
cuenta1=input('cuenta1: ')
cuenta2=input('cuenta2: ')
"""
cuentas=["unicornioazul","swishbish","gothem"]
hey=True
while(hey):
    for cuenta in cuentas:
        pa.cambiarVPNLogin(cuenta)
        if sf.ataque()>0:
            ataque=True
        else:
            ataque=False
        tl.enviarInformacionTelegram(cuenta,ataque)
        if cuenta=='unicornioazul':
           sf.tirarVacas()
        pa.subirPorDefecto()
        tl.enviarInformacionTelegram(cuenta,ataque)
        sf.salirDriver()

#cuenta='unicornioazul'
while(not hey):
    pa.cambiarVPNLogin(cuenta)
    if sf.ataque()>=0:
        ataque=True
    else:
        ataque=False
    tl.enviarInformacionTelegram(cuenta,ataque)
    while(True):
        sf.tirarVacas()
        pa.subirPorDefecto()
        tl.enviarInformacionTelegram(cuenta)
