import random

def zero_div(seq):
    start = seq.index(1)
    end = seq.index(1, start + 1)
    for _ in range(seq.count(1) - 1):
        yield end - start - 1
        if 1 not in seq[end + 1:]: return
        start = end
        end = seq.index(1, start + 1)


N = 10
sum_length = 0

list_test = [random.randrange(2) for _ in range(10)]
print(list_test)
for i in zero_div(list_test):
    print(i, end=' ')
    sum_length += i

print("\nAverage: " + str(round((sum_length / (list_test.count(1) - 1)), 3)))