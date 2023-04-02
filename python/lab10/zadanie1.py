# Celem programu jest implementacja automatu komórkowego 2D "Gra w życie". Tworzy się go na siatce kwadratowej N×N. Każda komórka może być w jednym z dwóch stanów
# 1 (żywa) lub 0 (martwa). Stosujemy periodyczne warunki brzegowe ("spinamy" krawędzie).

# Reguły:

#     martwa komórka, która ma dokładnie 3 żywych sąsiadów, staje się żywa w kolejnej iteracji
#     żywa komórka z 2 albo 3 żywymi sąsiadami pozostaje nadal żywa; przy innej liczbie żywych sąsiadów umiera

# Proszę utworzyć klasę, a w niej:

#     metodę inicjalizującą przyjmującą trzy parametry całkowite, pierwszy parametr określa rozmiary siatki, drugi wielkość początkowego kwadratu wypełnionego jedynkami, a trzeci liczbę iteracji,
#     metodę ewolucji automatu - w każdej iteracji ustalamy nowy stan każdej komórki, na podstawie stanu układu w kroku poprzednim,
#     metodę wypisującą na ekran stan układu - jeśli komórka jest żywa proszę wypisać * w przeciwnym wypadku spację.


# Proszę uruchomić program dla siatki 30x30 i "żywego" obszaru początkowego 10x10 oraz 11x11 (5p)


class Game:

    def __init__(self, n, m, i):
        self.n = n

        self.pole = [[0 for i in range(n)] for _ in range(n)]
        pass

    def evol(self):
        pass

    def __str__(self):
        for i in range(self.n):
            print(self.pole[i])



game = Game(30, 10, 1)
print(game)
