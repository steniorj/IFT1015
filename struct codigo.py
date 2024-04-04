class struct:

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return 'struct('+(', '.join(list(map(lambda f:f+'='+repr(self.__dict__[f]), self.__dict__))))+')'