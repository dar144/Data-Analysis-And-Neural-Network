# Proszę utworzyć klasę Wektor 3D, którego stan początkowy jest określony przez metodę 
# inicjalizacyjna. W klasie proszę zdefiniować metody przeciążające operatory dodawania, 
# odejmowania, mnożenia (mnożenie wektora przez liczbę) oraz metodę str. Proszę napisać także
# metody zwracające odpowiednio długość wektora, iloczyn skalarny, wektorowy i mieszany (4p).

import math

class Vector3D:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, vector):
        return Vector3D(self.x + vector.x,  self.y + vector.y, self.z + vector.z)

    def __sub__(self, vector):
        return Vector3D(self.x - vector.x,  self.y - vector.y, self.z - vector.z)

    def __mul__(self, num):
        return Vector3D(self.x * num,  self.y * num, self.z * num)
    __rmul__ = __mul__

    def lengthVec(self):
        return round(math.sqrt(pow(self.x, 2)+pow(self.y, 2)+pow(self.z, 2)), 2)

    def scalarMul(self, vector):
        return self.x * vector.x + self.y * vector.y + self.z * vector.z

    def vecMul(self, vector):
        return Vector3D(self.y * vector.z - self.z * vector.y, self.z * vector.x - self.x * vector.z,
        self.x * vector.y - self.y * vector.x) 

    def mixMul(self, vector1, vector2):
        return (self.vecMul(vector1)).scalarMul(vector2)

    def __str__(self):
        return f'x: {self.x}\ny: {self.y}\nz: {self.z}\n'



# vector1 = Vector3D(4, 8, 2)
# vector2 = Vector3D(2, 7, 3)

# print("Pierwszy wektor")
# print(vector1)

# print("Drugi wektor")
# print(vector2)

# print("Suma wektorow")
# print("vector1 + vector2")
# print(vector1 + vector2)
# print("vector2 + vector1")
# print(vector2 + vector1)

# print("Roznica wektorow")
# print("vector1 - vector2")
# print(vector1 - vector2)
# print("vector2 - vector1")
# print(vector2 - vector1)

# print("Mnożenie wektora przez liczbe")
# print("vector1 * 5")
# print(vector1 * 5)
# print("5 * vector2")
# print(5 * vector2)

# print("Dlugosc wektora")
# print("vector1")
# print(vector1.lengthVec())
# print("vector2")
# print(vector2.lengthVec())

# print("\nIloczyn skalarny")
# print(vector1.scalarMul(vector2))

# print("\nIloczyn wektorowy")
# vector3 = vector1.vecMul(vector2)
# print(vector3)

# print("Iloczyn mieszany")
# print(vector1.mixMul(vector2, vector3))


if __name__ == '__zadanie3__':
    pass



