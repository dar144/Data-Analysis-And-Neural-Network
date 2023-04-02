# unkcję dokonującą przekształcenia punktu na płaszczyźnie wg wzorów (ifs):
#   x(t+1)=a*x(t)+b*y(t)+c
#   y(t+1)=d*x(t)+e*y(t)+f
 
# Przykładowy zestaw współczynników (a,b,c,d,e,f):
# ((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236),
#  (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035))

# Przy kolejnych przekształceniach określoną szóstkę współczynników wybieramy odpowiednio z prawdopodobieństwem: (0.90, 0.05, 0.05). Proszę zgłosić wyjątek, jeżeli:

#     liczba zestawów współczynników jest różna od długości krotki z prawdopodobieństwami
#     suma prawdopodobieństw nie sumuje się do 1
#     któryś z zestawów współczynników na długość różną od 6


# Wynik proszę narysować (3p)

import matplotlib.pyplot as plt