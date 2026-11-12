# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:09:31 2026

@author: Admin
"""


import pandas as pd
import numpy as np
from scipy.stats import spearmanr
import seaborn as sns
import matplotlib.pyplot as plt

# --- Load your data ---
df = pd.read_excel("D:/Dissertation writing/Paper_2/HVI_Data_Arcmap2.xlsx", sheet_name="Sheet1")

# --- Baseline formula (raw HVI) ---
df['HVI_equal'] = df['Exposure Level'] + df['Sensitivity Level'] - df['Adaptive Capacity Level']

# --- Scenario 2: Exposure-dominant ---
df['HVI_exp'] = (2*df['Exposure Level'] + df['Sensitivity Level'] - df['Adaptive Capacity Level'])

# --- Scenario 3: Sensitivity-dominant ---
df['HVI_sens'] = (df['Exposure Level'] + 2*df['Sensitivity Level'] - df['Adaptive Capacity Level'])

# --- Scenario 4: Adaptive-dominant (stronger protection) ---
df['HVI_adapt'] = (df['Exposure Level'] + df['Sensitivity Level'] - 2*df['Adaptive Capacity Level'])

# --- Spearman rank correlation among scenarios ---
corr = df[['HVI_equal', 'HVI_exp', 'HVI_sens', 'HVI_adapt']].corr(method='spearman')

plt.figure(figsize=(6,5))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.show()

# --- Compare overlap of top 25% high-vulnerability districts ---
quantile_75 = df[['HVI_equal','HVI_exp','HVI_sens','HVI_adapt']].quantile(0.75)

top_overlap = {}
for col in df.columns[-4:]:
    top_overlap[col] = set(df.loc[df[col] >= quantile_75[col], 'NAME_2'])

base = top_overlap['HVI_equal']
for name, group in top_overlap.items():
    overlap = len(base.intersection(group)) / len(base) * 100
    print(f"Overlap of {name} with baseline = {overlap:.1f}%")



