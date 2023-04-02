# Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych
# (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć je dekoratorem 
# (implementowanym jako funkcja) sprawdzającym czy współrzędne leżą w określonym zakresie, 
# jeżeli nie - proszę zgłosić wyjątek (3p)

import zad1 as z

class IncorrectRange(Exception):
    """ Neprawidlowy zakres """
    pass

def dec(a, b):
    def fz(pf):
        def fw(p1, p2):
            if a <= p1.c[0] <= b and a <= p2.c[0] <= b and a <= p1.c[1] <= b and a <= p2.c[1] <= b:
                return pf(p1, p2)
            else:
                raise IncorrectRange()
        return fw
    return fz


@dec(1, 7)
def add(c1, c2):
    tmp = z.Coordinates()
    tmp.c = [c1.c[0]+c2.c[0], c1.c[1]+c2.c[1]]
    return tmp

@dec(1, 7)
def sub(c1, c2):
    tmp = z.Coordinates()
    tmp.c = [c1.c[0]-c2.c[0], c1.c[1]-c2.c[1]]
    return tmp



coord1 = z.Coordinates()
coord1.c = [1, 2]
print(coord1)

coord2 = z.Coordinates()
coord2.c = [3, 4]
print(coord2)

coord_add = add(coord1, coord2)
print(coord_add)

coord_sub = sub(coord1, coord2)
print(coord_sub)





