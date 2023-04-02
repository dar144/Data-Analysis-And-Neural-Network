# Proszę utworzyć klasę z metodami statycznymi obliczającymi obwód i pole trójkąta 
# lub czworokąta (dających się wpisać w okrąg, odpowiednio wzory Herona i Brahmagupty), 
# zdefiniowanych poprzez współrzędne wierzchołków (klasa z zadania 1) (3p)


# Wzór Herona: P=[p(p-a)(p-b)(p-c)]^1/2, gdzie: a,b,c - długości boków, p - połowa obwodu
# Wzór Brahmagupty: P=[(p-a)(p-b)(p-c)(p-d)]1/2, oznaczenia j.w.

import zad1 as z

class Figure:
    def __init__(self, c1, c2, c3, c4):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
    


coord1 = z.Coordinates()
coord1.c = [0, 0]

coord2 = z.Coordinates()
coord2.c = [0, 1]

coord3 = z.Coordinates()
coord3.c = [1, 1]

coord4 = z.Coordinates()
coord4.c = [1, 0]

f = Figure(coord1, coord2, coord3, coord4)
