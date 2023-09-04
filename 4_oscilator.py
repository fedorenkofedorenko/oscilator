import scipy as sp
import numpy as np
import math
import cmath


def a(n):
    """
    Boson creation operator 

    Args:
        n (1darray): ...
    """
    print(n)
    k = cmath.sqrt(n[1])
    n[1] = n[1]-1
    return k*n

def a_dag(n):
    """
    Boson annihilation operator 

    Args:
        n (1darray): ...
    """
    k = cmath.sqrt(n[1]+1)
    n[1] = n[1]+1
    return k*n

def hamiltonian(n, m, k, lam, om, h):
    """

    Args:
        n (1darray): _description_
    """
    # A = np.vectorize(a)
    # A_dag = np.vectorize(a_dag)
    p_x = complex(0,math.sqrt(h*m*om/2))*(a_dag(n)-a(n))
    x = math.sqrt(h/(2*m*om))*(a_dag(n)+a(n))
    H = p_x**2/2*m + k*x + lam*x**4
    print(H)
    return H

def matrix (n_r, step, m, k, lam, om, h):
    A = np.empty(n_r)
    for i in range(n_r[0], n_r[1],step):
        for j in range(n_r[0], n_r[1],step):
            # print(np.array([i,j]),np.array([[j],[i]]) ) - vectors are OK
            A[i,j]=np.array([[j],[i]])*hamiltonian(np.array([i,j]), m, k, lam, om, h)
    return A



def eigenvalue ():
    pass

def main(n_r, step, m, k, lam, om, h):
    M = matrix(n_r, step, m, k, lam, om, h)
    print (M)

main([0,4],1, 1, 1, 0.1, 1, 1)