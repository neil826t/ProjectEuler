import numpy as np

def prop_div(n):
    return np.array([i for i in range(1, n//2+1) if n%i==0])

def d(n):
    return sum(prop_div(n))

ami = set()
for a in range(10000):
    b = d(a)
    if d(b) == a and a!=b:
        ami.add(b)
        ami.add(a)
print(sum(ami))