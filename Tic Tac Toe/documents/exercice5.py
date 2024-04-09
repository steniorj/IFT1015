# Solution

"""
On peut se servir de la fonction retirerPointPoint (vue à la
démonstration de la semaine dernière) pour valider les path.

Il est à noter que les navigateurs font une élimination des ..
dans l'URL de la barre d'adresse.  Mais un hacker astucieux peux
passer par d'autres programmes, comme :

    % echo "GET /../serveur-web.py" | nc localhost 8000
	
"""


def retirerPointPoint(path):

    if len(path) == 0 or path[0] != '/':
        return None

    parties = []

    for partie in path[1:].split('/'):
        if partie == '..':
            if len(parties) == 0:
                return None
            parties.pop()
        else:
            parties.append(partie)

    return '/' + '/'.join(parties)

def obtenirDocument(path):
    pathSansPointPoint = retirerPointPoint(path)
    if pathSansPointPoint is None:
        return "le path n'est pas valide"
    else:
        return readFile('documents' + pathSansPointPoint)