# Proszę utworzyć klasę definiującą współrzędne punktu na płaszczyźnie.
# Obie współrzędne proszę zdefiniować jako własności (metoda inicjalizacyjna bezparametrowa) (1p)

class Coordinates:
    def __init__(self):
        self.c = [0, 0]

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c_0):
        self._c = c_0

    @c.getter
    def c(self):
        return self._c

    def __str__(self):
        return str(self.c)


if __name__ == '__zad2__':
    pass
