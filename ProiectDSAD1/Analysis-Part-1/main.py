import numpy as np
import pandas as pd
from geopandas import GeoDataFrame

from functii import *

vehicule = pd.read_csv("ProiectCSVnou.csv", index_col=0)

nan_replace(vehicule)
# print(vehicule)
variabile_vehicule = list(vehicule)[2:]

print(variabile_vehicule)
# print(vehicule.values)

vehicule_judete = vehicule[variabile_vehicule]

# print(vehicule_judete.values)

#Cerinta 1: Calculati procentajul tipurilor de vehicule inmatriculate in functie de judet si salvati in csv rezultatul
p = np.transpose(np.transpose(vehicule_judete.values) / np.sum(vehicule_judete.values, axis=1))
# print(p)
p_vehicule_judete = pd.DataFrame(p, vehicule["NumeJudet"], vehicule_judete.columns)
p_vehicule_judete.to_csv("procente_vehicule_judete.csv")


#Cerinta 2: Calculati procentajul tipurilor de vehicule inmatriculate in functie de regiune si salvati rezultatul in csv
coduri_regiuni = pd.read_csv("Coduri_Regiuni.csv", index_col=0)
# print(coduri_regiuni)
vehicule2 = vehicule.merge(right=coduri_regiuni, left_on="Regiune", right_index=True)
# print(vehicule2)
vehicule_regiuni = vehicule2[variabile_vehicule + ["Regiune"]].groupby(by="Regiune").agg(sum)
# print(vehicule_regiuni)
p = np.transpose(np.transpose(vehicule_regiuni.values)/ np.sum(vehicule_regiuni.values, axis=1))
p_vehicule_regiuni = pd.DataFrame(p, vehicule_regiuni.index, vehicule_regiuni.columns)
p_vehicule_regiuni.to_csv("procente_vehicule_regiuni.csv")


#Cerinta 3: Calculati procentajul tipurilor de vehicule inmatriculate in functie de macroregiune si salvati in csv
vehicule_macroReg = vehicule2[variabile_vehicule + ["MacroRegiune"]].groupby(by="MacroRegiune").agg(sum)
# print(vehicule_macroReg)
p = np.transpose(np.transpose(vehicule_macroReg.values)/ np.sum(vehicule_macroReg.values, axis=1))
p_vehicule_macroRegiuni = pd.DataFrame(p, vehicule_macroReg.index, vehicule_macroReg.columns)
p_vehicule_macroRegiuni.to_csv("procente_vehicule_macroregiuni.csv")


#Cerinta 4: Realizati harta si clasificati un criteriu (Tractoare) pe judete
gdf = GeoDataFrame.from_file("RO/RO_NUTS2/Ro.shp")
# print(gdf, list(gdf))
# gdf.to_csv("Geodataframe.csv")
gdf_ = gdf.merge(vehicule, left_on="snuts", right_index=True)
harta(gdf_, "Tractoare")


#Cerinta 5: Studiu 1 - Afisez judetele care au mai multe tractoare decat autobuze si microbuze
vehicule_s1 = vehicule[vehicule["Tractoare"] > vehicule["Autobuze_microbuze"]]
vehicule_s1[["NumeJudet", "Tractoare", "Autobuze_microbuze"]].to_csv("Studiu1.csv")

#Cerinta 6: Studiu 2 - Afisez pentru fiecare judet categoria de vehicule in care au fost inmatriculate cele mai putine vehicule
vehicule_s2 = vehicule.apply(func=categorie_minimala, axis=1, vehicule=variabile_vehicule)
vehicule_s2.to_csv("Studiu2.csv")

#Cerinta 7: Studiu 3 - Afisez judetele cu autoturisme intre 100000 si 300000, apoi realizez harta pentru judetele in cauza
vehicule_s3 = vehicule[vehicule["Autoturisme"] > 100000]
# print(vehicule_s3)
vehicule_s4 = vehicule_s3[vehicule_s3["Autoturisme"] < 300000]
# print(vehicule_s4)
vehicule_s4[["NumeJudet", "Autoturisme"]].to_csv("Studiu3.csv")
gdf = GeoDataFrame.from_file("RO/RO_NUTS2/Ro.shp")
gdf_ = gdf.merge(vehicule_s4, left_on="snuts", right_index=True)
harta(gdf_, "Autoturisme")



#Cerinta 8: Realizati PieChart pe macroregiune
for i in range(0, len(vehicule_macroReg.index)):
    # print(vehicule_macroReg.iloc[i].values)
    pieChart(vehicule_macroReg.iloc[i].values, variabile_vehicule, titlu="Macroregiune " + str(i+1))


#Cerinta 9: Realizati matrice de corelatie pentru macroregiuni
vehicule_ = vehicule[variabile_vehicule + ["Regiune"]].merge(coduri_regiuni, left_on="Regiune", right_index=True)
# print(vehicule_)
vehicule_correl = vehicule_.groupby(by="MacroRegiune").apply(func=corelatie)
# print(vehicule_correl[variabile_vehicule])

for v in vehicule_correl.index.get_level_values(0).unique():
    # print(vehicule_correl.loc[v,:])
    vehicule_correl.loc[v, :].to_csv("Macroregiune" + str(v) + ".csv")


#Cerinta 10: Realizati corelograme pentru macroregiuni
for v in vehicule_correl.index.get_level_values(0).unique():
    corelograma(vehicule_correl.loc[v, :], titlu="Corelograma macroregiune " + str(v))

