nom = "**pas de nom**"

def clic():
    alert("Bonjour "+nom+"!")

def init():
    global nom
    nom = prompt("Votre nom?")
