import sympy
import random
from sympy import sieve
import numpy as np

# seed = random.randint(1,1e10)


def cal_con_primes(_from,_to, N):
    con_primes = [i for i in sieve.primerange(_from, _to) if(i % 4 == 3)]
    p,q = np.random.choice(con_primes,2)
    while(p*q<N):
        p,q = np.random.choice(con_primes,2)
    return p,q


def randomNumbers(N,p,q, seed):
    index = []
    M = p*q
    x = seed

    for _ in range(N):
        index.append(x%N)
        x = x*x % M
    return index

p,q = cal_con_primes(2,42000,6000)
N = 6000

print(p,q)
# print(randomNumbers(6000,p,q,random.randint(1,1e10)))



