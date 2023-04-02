# Proszę napisać iterator liczb pseudolosowych. Ciąg taki otrzymujemy ze wzoru:
# Xn+1 = (aXn + c) mod m, dla m = 231-1, a = 75, c = 0, x0 = 1.

# Korzystając z zaimplementowanego iteratora proszę wylosować 10^5 par liczb 
# z przedziału [0,1). Proszę sprawdzić jaki procent wylosowanych par mieści się w
#  kwadracie o boku 0.1*n, gdzie n∈[1,10]. Otrzymany wynik proszę porównać z wynikiem 
#  uzyskiwanym z wykorzystaniem generatora liczb pseudolosowych z języka Python (4p).

class Pseudolosowe:
    def __init__(self, m, a, c, x_0, stop):
        self.m = m  
        self.a = a 
        self.c = c    
        self.x_0 = x_0
        self.start = 0
        self.stop = stop
        self.x = ((a * x_0 + c) % m) / m

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.stop:
            self.start += 1
            if self.x < 1:
                self.x = ((self.a * self.x + self.c) % self.m) / self.m
                return self.x 
        raise StopIteration
     

los = Pseudolosowe(2**31-1, 7**5, 0, 1, 1)

for _ in range(100000):
    for _ in range(2):
        for l in los:
            
        




