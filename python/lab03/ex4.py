import random
import sys
import string

print("\n*************zad1*************")
def fun_zad1(text):
    l = []
    for i in string.ascii_lowercase:
        if i in text and i != 'x':
            tr = str.maketrans(i, str(random.randrange(0, 10)))
            text = text.translate(tr)
    print(text)

    l = [(random.uniform(0,5), eval(text.translate({120: str(random.uniform(0,5))}))) for i in range(10)]
    print(l)


if len(sys.argv) != 1:
    text = sys.argv[1]
else:
    print("Nie ma elementow listy argv")

text = fun_zad1(text)




print("\n*************zad2*************")
def fun_zad2(*d):
    k = []
    for i in range(len(d)):
        if d[0][i] in d[i]:
            k.append(d[0][i])
    else:
        pass

    # k = [d[0][i] for i in range(len(d)) if d[0][i] in d[i]]
    return k
    
lista = fun_zad2([1,2,3], (1,3,5), [3,2])

print(lista)




print("\n*************zad3*************")
def fun_zad3(a, b, c=True):
    print("ala")



