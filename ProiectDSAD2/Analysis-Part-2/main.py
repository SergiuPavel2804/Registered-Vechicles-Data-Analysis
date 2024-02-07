import pandas as pd
from geopandas import GeoDataFrame

from hclust import hclust
from functii import *

tabel = pd.read_csv("Autovehicule.csv", index_col=0)
nan_replace_t(tabel)
# print(tabel)
variabile = list(tabel)[1:]
# print(variabile)

model_hclust = hclust(tabel, variabile)
#componenta partitiei optime
p_opt = model_hclust.calcul_partitie()
# print(p_opt)

#dendrograme
plot_ierarhie(model_hclust.h, tabel.index, model_hclust.threshold)
tabel_partitii = pd.DataFrame(data={
    "P_Opt": p_opt
}, index=tabel.index)
# print(tabel_partitii)

p4 = model_hclust.calcul_partitie(4)
plot_ierarhie(model_hclust.h, tabel.index, model_hclust.threshold)

tabel_partitii["P4"] = p4
# print(tabel_partitii["P4"])

p5 = model_hclust.calcul_partitie(5)
plot_ierarhie(model_hclust.h, tabel.index, model_hclust.threshold)
tabel_partitii["P5"] = p5
# print(tabel_partitii["P5"])

p6 = model_hclust.calcul_partitie(6)
plot_ierarhie(model_hclust.h, tabel.index, model_hclust.threshold)
tabel_partitii["P6"] = p6
# print(tabel_partitii["P6"])

#histograme
for v in variabile:
    # histograme(tabel[v].values,p_opt,v)
    # histograme(tabel[v].values, p4, v)
    histograme(tabel[v].values, p5, v)
    # histograme(tabel[v].values, p6, v)

#harta clusteri
gdf = GeoDataFrame.from_file("RO/RO_NUTS2/Ro.shp")
gdf_ = gdf.merge(tabel_partitii, left_on="snuts", right_index=True)
# print(gdf_)
harta(gdf_, "P4")

show()