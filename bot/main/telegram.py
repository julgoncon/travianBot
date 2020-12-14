import requests
import seleniumFunct as sf
def generarText(recur,prod,cuenta,ataque):
    if ataque:
        txt='ESTA SIENDO ATACADA\n'
    else:
        txt=''
    text=txt+cuenta+'====\n\nrecursos:\nmadera= '+str(recur[0])+'/'+str(recur[4][0])+'\nbarro= '+str(recur[1])+'/'+str(recur[4][0])+'\nhierro= '+str(recur[2])+'/'+str(recur[4][0])+'\ncereal= '+str(recur[3])+'/'+str(recur[4][1])+'\n\nproduccion:\nmadera= '+str(prod[0])+'\nbarro= '+str(prod[1])+'\nhierro= '+str(prod[2])+'\ncereal= '+str(prod[3])
    return text
def enviarMensaje(text):
    requests.post('https://api.telegram.org/[telegram-bot-token]/sendMessage',
              data={'chat_id': '-434698632', 'text': text})

def enviarInformacionTelegram(cuenta,ataque):
    prod=sf.produccion()
    recur=sf.recursosDisponibles()
    text=generarText(recur,prod,cuenta,ataque)
    enviarMensaje(text)
