def clic():
    nom = document.querySelector('#nom').value
    if document.querySelector('#sexe').value == 'H':
        alert('Bonjour M. ' + nom)
    else:
        alert('Bonjour Mme. ' + nom)
