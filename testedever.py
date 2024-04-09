mois = ['jan','feb','mar','apr','may','jun',
        'jul','aug','sep','oct','nov','dec']

def ol(contenu): return '<ol>' + contenu + '</ol'

def li(contenu): return '<li>' + contenu + '</li>'

print(list(map(li,mois)))
print(ol(''.join(list(map(li,mois)))))