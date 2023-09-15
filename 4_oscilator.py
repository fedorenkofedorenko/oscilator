import numpy as np
from scipy.linalg import eigvalsh
import cmath

def H_mn (n):
    h_mn = 1/(2**(1/2))*(n+1/2)
    return h_mn

def V (m,n, n_max, lam):
    el = 0
    if m == n+4:
        if n<=n_max-4:
            el+= ((n+1)*(n+2)*(n+3)*(n+4))**(1/2)
    if m == n+2:
        el+= n**2
        if n<= n_max-2:
            el+= ((n+n+1+n+2)*((n+1)*(n+2))**(1/2))
        if n <= n_max-3:
            el += ((n+3)*((n+1)*(n+2))**(1/2))
    if m == n:
        el+= n**2
        if n>0:
            el+= n*(n-1)
        if n<n_max:
            el+= 2*n*(n+1)+(n+1)**2
        if n<= n_max-2:
            el+=(n+1)*(n+2)
    if m == n-2:
        if n>=2:
            el+= (n*(n-1))**(1/2)*(n-2+n-1+n)
            if n< n_max :
                el += (n*(n-1))**(1/2)*(n+1)
    if m == n-4:
        if n>=4:
            el+= (n*(n-1)*(n-2)*(n-3))**(1/2)    
    el*=lam*1/4
    return el

def matrix(n_max, lam):
    H = np.zeros((n_max, n_max), dtype=float)
    for i in range(0,n_max):
        H[i,i] = float(H_mn(i))
        for j in (1, n_max-1):
            H[i, j] = float(H_mn(j) + V(i,j,n_max, lam))
    return H

def main(n_max, lam):
    M = matrix(n_max, lam)
    # M.tofile("matrix.dat", "    ")
    v = eigvalsh(M, subset_by_index = [0,1])
    v.tofile("eigenvalues_lam_"+str(lam)+".dat", "    ")
    print (v)

main(500, 0.6)