
import matplotlib.pyplot as plt

x = []
y = []
std = []

with open('data.out') as file_object:
    for line in file_object:
        line = line.split()
        x.append(int(line[0]))
        y.append(float(line[1]))
        std.append(float(line[2]))

plt.plot(x, y, 'o')
plt.errorbar(x, y, marker='*', yerr=std)
plt.xlabel('x')
plt.savefig('res.pdf')        
        