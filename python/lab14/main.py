import sys
sys.path.append('build/lib.linux-x86_64-3.9')

import mod
import random
import time
import copy

# ZADANIE 1
print(mod.met(1,2))
print(mod.met(1,2,5))
print(mod.met(1,2,5,[2,3,4]))



# ZADANIE 2
def PySort(arr, n):
    for i in range(1, n):
        add_el = arr[i]
        j = i-1
        while j >= 0 and arr[j]>add_el:
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1]=add_el

# py_time = 0
# c_time = 0

# size = [10,10**2,10**3, 10**4]
# for k in range(len(size)):
#     tab1 = [random.randint(0,size[k]) for _ in range(size[k])]
#     tab2 = copy.deepcopy(tab1)

#     t1= time.time()
#     PySort(tab1,size[k])
#     t2=time.time()
#     py_time+=t2-t1

#     t3= time.time()
    # tab2 = mod.CSort(tab2,size[k])
    # t4=time.time()
    # c_time+=t4-t3


tab1 = [random.randint(0,10) for _ in range(10)]
tab2 = copy.deepcopy(tab1)
print("\nPython")
print(tab1)
PySort(tab1,10)
print(tab1)

print("\nC")
print(tab2)
print(mod.CSort(tab2,10))













# size = [10,10**2,10**3, 10**4]
# for k in range(len(size)):
#     tab = [random.randint(0,size[k]) for _ in range(size[k]+1)]