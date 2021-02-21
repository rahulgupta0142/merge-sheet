import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


pf1=pd.read_csv("sheet_01.csv")
pf2=pd.read_csv("sheet_01.csv")
print(pf1)
print(pf2)



pd.merge(pf1,pf2)
