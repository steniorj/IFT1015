def init():
    global msg
    msg = document.querySelector('#msg')
    msg.innerHTML = 'bonjour'

def clic():
    msg.innerHTML = '*' + msg.innerHTML + '*'

