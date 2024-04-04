class struct:

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return 'struct('+(', '.join(list(map(lambda f:f+'='+repr(self.__dict__[f]), self.__dict__))))+')'

alignements = [struct(pas= +1, departs= [0,3,6]),
               struct(pas= +3, departs= [0,1,2]),
               struct(pas= +4, departs= [0]),
               struct(pas= -2, departs= [6])]

def victoire():

    for alignement in alignements:

        pas = alignement.pas

        for pos in alignement.departs:
            print('pos= ',pos)


victoire()

alignements = [[0,3,6],[0,1,2]]
pas = 1
sym = ['x','o','x','x','x','x','x','x','x']
print(sym[3])
for i in range(6):
    print(i)
    if i == 6:
        break
else:
    print('pp')

