# print("************* zad1 *************")

import time
import sys

powt = 1000
N = 10000

def forStatement():
    # dodawanie elementu
    seq = []
    for i in range(N):
        seq.append(i)

    # dodawanie elementu podniesionego do kwadratu
    seq = []
    for i in range(N):
        seq.append(i**2)

    # sumowanie elementów z wykorzystaniem pętli for
    suma = 0
    for i in range(N):
        suma += seq[i]

    # sumowanie z wykorzystaniem funkcji sum
    suma = sum(seq)



def listComprehension():
    # dodawanie elementu
    seq = [i for i in range(N)]

    # dodawanie elementu podniesionego do kwadratu
    seq = [i**2 for i in range(N)]

    # sumowanie elementów z wykorzystaniem pętli for
    suma = 0
    for i in range(N):
        suma += seq[i]

    # sumowanie z wykorzystaniem funkcji sum
    suma = sum(seq)



def mapFunction():
    # dodawanie elementu
    seq = list(map(lambda x: x, range(N)))

    # dodawanie elementu podniesionego do kwadratu
    seq = list(map(lambda x: x**2, range(N)))

    # sumowanie elementów z wykorzystaniem pętli for
    suma = 0
    for i in range(N):
        suma += seq[i]

    # sumowanie z wykorzystaniem funkcji sum
    suma = sum(seq)



def generatorExpression():
    # dodawanie elementu
    seq = list((i for i in range(N)))

    # dodawanie elementu podniesionego do kwadratu
    seq = list((i**2 for i in range(N)))

    # sumowanie elementów z wykorzystaniem pętli for
    suma = 0
    for i in range(N):
        suma += seq[i]

    # sumowanie z wykorzystaniem funkcji sum
    suma = sum(seq)



def tester(fun):
    start = time.time_ns()

    for i in range(powt):
        fun()

    end =  time.time_ns()

    return end - start


print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))



# dla jednej konwersji obiektu map i generatora do listy

# forStatement         => 2810766172
# listComprehension    => 2614873844
# mapFunction          => 2509793636
# generatorExpression  => 2406048431



# dla dwoch konwersji obiektu map i generatora do listy

# forStatement         => 2856141051
# listComprehension    => 2597622202
# mapFunction          => 3079734512
# generatorExpression  => 3045547632