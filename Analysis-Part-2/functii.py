import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
import pandas as pd
from pandas.api.types import is_numeric_dtype

def nan_replace_t(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

def plot_ierarhie(h,etichete,threshold):
    fig  = plt.figure(figsize=(9,6))
    ax = fig.add_subplot(1,1,1)
    ax.set_title("Dendrograma")
    dendrogram(h,labels=etichete,ax=ax,color_threshold=threshold)

def histograme(z,p,variabila):
    fig  = plt.figure(figsize=(9,6))
    assert isinstance(fig,plt.Figure)
    fig.suptitle("Histograme pentru variabila "+variabila)
    clase = np.unique(p)
    q = len(clase)
    axe = fig.subplots(1,q,sharey=True)
    for i in range(q):
        axe[i].set_xlabel(clase[i])
        axe[i].hist(x=z[p==clase[i]],rwidth=0.9,range=(min(z),max(z)))
    plt.show()

def harta(t, coloana):
    t.plot(column=coloana, legend=True)
    plt.show()

def show():
    plt.show()