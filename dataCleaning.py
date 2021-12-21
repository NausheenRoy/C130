import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Luminosity"]
df.drop(["Star_name","Distance","Mass","Radius"])
df.dropna()



df.to_csv('cleadedData.csv') 