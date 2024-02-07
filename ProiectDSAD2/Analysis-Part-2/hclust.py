import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage


class hclust():
    def __init__(self, t, variabile, metoda="complete"):
        self.x = t[variabile].values
        self.h = linkage(self.x, method=metoda)

    def calcul_partitie(self, k=None):
        nr_jonctiuni = self.h.shape[0]
        n = nr_jonctiuni + 1
        if k is None:
            k_max = np.argmax(self.h[1:, 2] - self.h[:(nr_jonctiuni - 1), 2])
            k = nr_jonctiuni - k_max
        else:
            k_max = nr_jonctiuni - k
        self.k = k
        self.threshold = (self.h[k_max, 2] + self.h[k_max + 1, 2]) / 2
        c = np.arange(n)
        for j in range(nr_jonctiuni-k+1):
            k1 = self.h[j, 0]
            k2 = self.h[j, 1]
            c[c == k1] = n + j
            c[c == k2] = n + j
        coduri = pd.Categorical(c).codes
        return np.array( ["c"+str(i+1) for i in coduri] )