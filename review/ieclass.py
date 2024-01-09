# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:32:01 2023

@author: KAM8BP
"""
import matplotlib.pyplot as plt
import pandas as pd

# Load data from file using Pandas
df1 = pd.read_csv("ie1.csv")
df2 = pd.read_csv("ie2.csv")
df3 = pd.read_csv("ie3.csv")
df4 = pd.read_csv("ie4.csv")
plt.figure(figsize=(6, 4))
# Plot the efficiency vs. logarithmic scale using a logarithmic x-axis
plt.semilogx(df1.iloc[:,0], df1.iloc[:,1], label='IE1', color='#ED0007')
plt.semilogx(df2.iloc[:,0], df2.iloc[:,1], label='IE2', color='#D6451C')
plt.semilogx(df3.iloc[:,0], df3.iloc[:,1], label='IE3', color='#6B7F3F')
plt.semilogx(df4.iloc[:,0], df4.iloc[:,1], label='IE4', color='#00884A')

plt.fill_between(df1.iloc[:,0], df1.iloc[:,1], df2.iloc[:,1], alpha=0.2, color='#ED0007')
plt.fill_between(df1.iloc[:,0], df2.iloc[:,1], df3.iloc[:,1], alpha=0.2, color='#D6451C')
plt.fill_between(df1.iloc[:,0], df3.iloc[:,1], df4.iloc[:,1], alpha=0.2, color='#6B7F3F')
plt.fill_between(df4.iloc[:,0], df4.iloc[:,1], 100, color='#00884A', alpha=0.2)


plt.xlabel("Rated power [kW]", fontsize=12)
plt.ylabel("Efficiency [%]", fontsize=12)
plt.legend(fontsize=12, loc='lower right')
plt.grid(True, which='both', linestyle='--', alpha=0.5)
plt.minorticks_on()
plt.grid(True, which='minor', linestyle=':', alpha=0.5)

# Increase tick labels font size to 12
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=12)

plt.savefig("myfigure.png", dpi=300, bbox_inches="tight")