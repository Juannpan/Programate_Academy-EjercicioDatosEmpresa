#importar librerias
import pandas as pd
import numpy as np
import matplotlib as mpl

#importar base de datos
dfv1 = pd.read_csv('Database/ventas-1-65d374724924b571259206.csv')
dfv2 = pd.read_csv('Database//ventas-2-65d374947fb4d216940241.csv')

#Limpieza de datos
dfv1.isnull().sum()