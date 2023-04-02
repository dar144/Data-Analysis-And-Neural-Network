# print("************* zad2 *************")

import random
import math

# promien kola
r = 1

# bok kwadratu
a = 2

# punkty 
points = [(random.uniform(-1, 1), random.uniform(-1, 1)) for i in range(100000)]

# liczba trafien kwadratu oraz kola
t_kolo = len(list(filter(lambda point: math.sqrt(point[0]**2 + point[1]**2) < r, points)))
t_kwadrat = len(points)


pi = 4*(t_kolo / t_kwadrat)
print(pi)