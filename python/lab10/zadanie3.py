# Proszę utworzyć funkcje obliczające odpowiednio (jako parametry przekazujemy obiekty wcześniej utworzonej klasy) (1p):

#     strumień indukcji magnetycznej: Φ=B•S
#     siłę Lorentza F=q(E+v × B)
#     pracę siły Lorentza W=qE•v

import zadanie2 as z

B = z.Vector3D(4, 8, 2)
S = z.Vector3D(2, 7, 3)
E = z.Vector3D(1, 2, 3)
v = z.Vector3D(3, 4, 5)

q = 1.6 * 10e-19

Φ = B.scalarMul(S)
print("Strumień indukcji magnetycznej: " + str(Φ) + " Wb")

F = q*(E + v.vecMul(B)).lengthVec()
print("Sila Lorentza: " + str(F) + " N")

W = (q * E).scalarMul(v)
print("Praca sily Lorentza: " + str(W) + " J")
