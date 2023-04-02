# Proszę napisać funkcję, która pozwoli na wypisanie: n początkowych wierszy pliku, n końcowych wierszy pliku,
# co n-tego wiersza pliku, n-tego słowa ze wszystkich wierszy i n-tego znaku ze wszystkich wierszy. 
# Nazwę pliku oraz n przekazujemy jako parametr do funkcji. Każdy podpunkt==jedna linia kodu (1.5p)

def fun(namefile, n):
    with open(namefile) as file_object:
        f = file_object.readlines()
        print(f[:n])                                                # n początkowych wierszy pliku
        print(f[-n:])                                               # n końcowych wierszy pliku
        print(f[n-1::n])                                            # co n-tego wiersza pliku
        print([el.split()[n-1] for el in f if n >= len(el)])        # n-tego słowa ze wszystkich wierszy
        print([el[n-1] for el in f])                                # n-tego znaku ze wszystkich wierszy


fun('data/data0.in', 2)