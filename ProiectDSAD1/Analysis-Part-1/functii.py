import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.api.types import is_numeric_dtype
from seaborn import heatmap


def nan_replace(t):
    assert isinstance(t, pd.DataFrame)
    for v in t.columns:
        if any(t[v].isna()):
            if is_numeric_dtype(t[v]):
                t[v].fillna(t[v].mean(), inplace=True)
            else:
                t[v].fillna(t[v].mode()[0], inplace=True)

def harta(t, coloana):
    t.plot(column=coloana, legend=True)
    plt.show()

def categorie_minimala(t, vehicule):
    x = t[vehicule].values
    k = np.argmin(x)
    return pd.Series([t.loc["NumeJudet"], vehicule[k]], ["Nume judet", "Categoria minimala"])


def pieChart(t, variabile, titlu):
    figureObject, axesObject = plt.subplots()
    explodeTuple = (0.4 , 0.1, 0.0, 0.0, 0.4 , 0.8, 0.0)
    axesObject.pie(t, explode=explodeTuple, labels=variabile, autopct='%1.2f', startangle=90)
    axesObject.axis('equal')
    plt.title(titlu)
    plt.show()

def corelatie(t):
    assert isinstance(t, pd.DataFrame)
    return t.corr()


def corelograma(t, cmap="RdYlBu", titlu="Grafic corelograma"):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(1, 1, 1)
    assert isinstance(ax, plt.Axes)
    ax.set_title(titlu, fontdict={"fontsize": 18, "color": "b"})
    heatmap(t, vmin=-1, vmax=1, annot=True, cmap=cmap, ax=ax)
    plt.show()
