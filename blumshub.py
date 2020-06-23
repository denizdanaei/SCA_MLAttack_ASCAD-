import sympy
import random
from sympy import sieve
import numpy as np

# seed = random.randint(1,1e10)


def cal_con_primes(_from,_to, testSize):
    con_primes = [i for i in sieve.primerange(_from, _to) if(i % 4 == 3)]
    p,q = np.random.choice(con_primes,2)
    while(p*q<testSize & p*q>_to):
        p,q = np.random.choice(con_primes,2)
    return p*q

def randomNumbers(N, M):
    index = []
    x = random.randint(1, 1e10)

    for _ in range(N):
        index.append(x%N)
        x = x*x % M
    return index


M = cal_con_primes(2,32999,12000)
N = 6000

# print(p,q)
print(i for i in randomNumbers(12000,M)  if (isinstance(i, float)))



