# Proszę utworzyć dekorator (implementowany jako klasa) umożliwiający zliczenie liczby
# wywołań poszczególnych 
# funkcji obłożonych dekoratorem, z metodą statyczną zwracającą wynik (3p)

class Num:
    _n = 0

    def __init__(self, pf):
        self._pf = pf
        self._n = 0

    def __call__(self, p):
        Num._n += 1
        def fw(p):
            return Num._pf(p)
        return fw

    @staticmethod
    def final():
        return Num._n
    

@Num
def fsum(p):
    return sum(p)

@Num
def rsum(p):
    return sum(filter(lambda x: x%2, p))


fsum(range(10))
fsum(range(10))
fsum(range(10))
print(fsum.final())

rsum(range(10))
rsum(range(10))
print(rsum.final())

