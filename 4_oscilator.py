import scipy as sp
import numpy as np
from scipy.linalg import eigvalsh
import math
import cmath


def a(n): 
    """
    Boson creation operator 

    Args:
        n (1darray): ...
    """
    print(n)
    k = cmath.sqrt(n[0])
    return k

def a_dag(n):
    """
    Boson annihilation operator 

    Args:
        n (1darray): ...
    """
    k = cmath.sqrt(n[0]+1)
    return k

def hamiltonian(n, lam, om, ):
    """

    Args:
        n (1darray): _description_
    """
    H = -om ** 2/2*((a_dag(n)**2+a(n)**2-1)/(a_dag(n)+a(n))) + 1/4*om**2*(a_dag(n)**2+a(n)**2+1)+lam/(16*om**4)*(a_dag(n)**2+a(n)**2+1)**2
    return H

def matrix (n_r, step, lam, om):
    A = np.empty((n_r[1],n_r[1]))
    for i in range(n_r[0], n_r[1],step):
        for j in range(n_r[0], n_r[1],step):
            # print(np.array([i,j]),np.array([[j],[i]]) ) #- vectors are OK
            A[i, j] = hamiltonian(np.array([[j], [i]]), lam, om).real
    return A



def eigenvalue (A):
    vals = eigvalsh(A, subset_by_index= [0,1])
    return vals
def main(n_r, step,lam, om):
    M = matrix(n_r, step, lam, om )
    v = eigenvalue(M)
    print (v)

main([1,10],1, 1, 1)