# Proszę napisać iterator zwracający kolejne liczby pierwsze z zadanego zakresu dwoma 
# sposobami i porównać ich wykorzystanie (1p).

class Pierwsze:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            self.start += 1
            count = 0 
            if self.start-1 == 1:
                return 1
            else:
                for i in range(2, self.start):
                    if (self.start-1) % i == 0:
                        count += 1
                if count == 0:
                    return self.start-1
        raise StopIteration


pierw = Pierwsze(7, 20)
for p in pierw:
    print(p)


