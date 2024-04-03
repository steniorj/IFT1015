def init():
    global msg
    msg = document.querySelector('#msg')
    msg.innerHTML = 'bonjuju'

def clic():
    msg.innerHTML = '*' + msg.innerHTML + '*'

def clic2():
    msg2 = document.querySelector('#msg2')
    msg2.innerHTML = "papara"
    msg2.innerHTML = '-=' + msg.innerHTML + '=-'