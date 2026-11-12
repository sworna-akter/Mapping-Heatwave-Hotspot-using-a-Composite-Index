# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:56:19 2026

@author: Admin
"""

####Statistical analyis of HVI
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib.gridspec as gridspec

# =======================
# Load the data
# =======================
hvi_file = "D:/Dissertation writing/Paper_2/HVI_D.xlsx"

df_hvi = pd.read_excel(hvi_file, sheet_name="HVI")
df_division = pd.read_excel(hvi_file, sheet_name="Division_HVI")
df_district = pd.read_excel(hvi_file, sheet_name="Sheet11")

# Strip column names to avoid KeyErrors
df_hvi.columns = df_hvi.columns.str.strip()
df_division.columns = df_division.columns.str.strip()
df_district.columns = df_district.columns.str.strip()

# =======================
# Create figure and GridSpec
# =======================
fig = plt.figure(figsize=(18, 12))
gs = gridspec.GridSpec(2, 2, wspace=0.3, hspace=0.4)

# =======================
# (a) Histogram + normal curve
# =======================
ax1 = fig.add_subplot(gs[0, 0])
hvi_data = df_hvi['HVI'].dropna()
mean_hvi = hvi_data.mean()
std_hvi = hvi_data.std()

ax1.hist(hvi_data, bins=30, density=True, alpha=0.6, color='skyblue', label='HVI Distribution')
x = np.linspace(hvi_data.min(), hvi_data.max(), 100)
p = norm.pdf(x, mean_hvi, std_hvi)
ax1.plot(x, p, 'k', linewidth=2, label=f'Normal Dist.\nMean={mean_hvi:.2f}, Std={std_hvi:.2f}')
ax1.set_xlabel('HVI', fontsize=16)
ax1.set_ylabel('Density', fontsize=16)
ax1.set_title('(a)', fontsize=18, loc='center')
ax1.legend(fontsize=12)
ax1.tick_params(axis='both', labelsize=14)
ax1.grid(True)

# =======================
# (b) Boxplot
# =======================
ax2 = fig.add_subplot(gs[0, 1])
min_hvi = df_hvi['HVI'].min()
q1_hvi = df_hvi['HVI'].quantile(0.25)
median_hvi = df_hvi['HVI'].median()
q3_hvi = df_hvi['HVI'].quantile(0.75)
max_hvi = df_hvi['HVI'].max()

ax2.boxplot(df_hvi['HVI'], vert=True, patch_artist=True,
            boxprops=dict(facecolor='Skyblue', color='Skyblue'),
            medianprops=dict(color='red', linewidth=2),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', color='red', markersize=8))
ax2.set_ylabel('HVI', fontsize=16)
ax2.set_title('(b)', fontsize=18, loc='center')
ax2.tick_params(axis='y', labelsize=14)

# Annotate statistics
ax2.text(1.1, min_hvi, f'Min: {min_hvi:.2f}', verticalalignment='center', color='black', fontsize=12)
ax2.text(1.1, q1_hvi, f'Q1: {q1_hvi:.2f}', verticalalignment='center', color='black', fontsize=12)
ax2.text(1.1, median_hvi, f'Median: {median_hvi:.2f}', verticalalignment='center', color='red', fontsize=12)
ax2.text(1.1, q3_hvi, f'Q3: {q3_hvi:.2f}', verticalalignment='center', color='black', fontsize=12)
ax2.text(1.1, max_hvi, f'Max: {max_hvi:.2f}', verticalalignment='center', color='black', fontsize=12)
ax2.grid(True)

# =======================
# (c) Division-level bar chart
# =======================
ax3 = fig.add_subplot(gs[1, 0])
bar_width = 0.25
index = np.arange(len(df_division))
ax3.bar(index, df_division['Exposure Level'], bar_width, label='Exposure Level', color='salmon')
ax3.bar(index + bar_width, df_division['Sensitivity Level'], bar_width, label='Sensitivity Level', color='skyblue')
ax3.bar(index + 2*bar_width, df_division['Adaptive Capacity Level'], bar_width, label='Adaptive Capacity Level', color='green')

ax3.set_xlabel("Division", fontsize=16)
ax3.set_ylabel("Level", fontsize=16)
ax3.set_xticks(index + bar_width)
ax3.set_xticklabels(df_division['Division'], rotation=45, ha='right', fontsize=14)
ax3.set_title('(c)', fontsize=18, loc='center')
ax3.legend(fontsize=12)
ax3.grid(axis='y')

# =======================
# (d) Horizontal bar plot of HVI across districts
# =======================
ax4 = fig.add_subplot(gs[1, 1])
ax4.barh(df_district['Division'], df_district['HVI'], color='Skyblue')
ax4.set_xlabel("HVI", fontsize=16)
ax4.set_ylabel("Division", fontsize=16)
ax4.set_title('(d)', fontsize=18, loc='center')
ax4.tick_params(axis='both', labelsize=14)
ax4.grid(axis="x", linestyle="--", alpha=0.7)

# =======================
# Show all plots
# =======================
plt.tight_layout()
plt.show()






#Relationship coefficient of HVI with indices

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the Excel file

data_file = "D:\MY RE\Dissertation writing\Paper_1\HVI_Data/HVI_D.xlsx"  # Replace with your file name
df = pd.read_excel(data_file, sheet_name="HVI")

# Prepare the data for linear regression
X = df['Exposure Level'].values.reshape(-1, 1)  # Independent variable
y = df['HVI'].values  # Dependent variable

# Perform linear regression
model = LinearRegression()
model.fit(X, y)

# Generate predictions and calculate R²
y_pred = model.predict(X)
r_squared = model.score(X, y)

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, c='blue', alpha=0.6, label='Data points')

# Plot the regression line with R²
plt.plot(X, y_pred, color='red', linewidth=2, 
         label=f'Regression Line: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}\n$R^2$ = {r_squared:.2f}')

# Labels and title
plt.xlabel('Exposure')
plt.ylabel('HVI')
plt.legend(fontsize=13, loc='lower right')
plt.grid(True)

# Show the plot
plt.show()





import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the Excel file
data_file = "D:/Dissertation writing/Paper_2/HVI_D.xlsx"  # Replace with your file name
df = pd.read_excel(data_file, sheet_name="Sheet1")

# Prepare the data for linear regression
X = df['Sensitivity Level'].values.reshape(-1, 1)  # Independent variable
y = df['HVI'].values  # Dependent variable

# Perform linear regression
model = LinearRegression()
model.fit(X, y)

# Generate predictions and calculate R²
y_pred = model.predict(X)
r_squared = model.score(X, y)

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, c='blue', alpha=0.6, label='Data points')

# Plot the regression line with R²
plt.plot(X, y_pred, color='red', linewidth=2, 
         label=f'Regression Line: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}\n$R^2$ = {r_squared:.2f}')

# Labels and title
plt.xlabel('Sensitivity')
plt.ylabel('HVI')
plt.legend(fontsize=13, loc='lower right')
plt.grid(True)

# Show the plot
plt.show()





import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the Excel file
data_file = "D:/Dissertation writing/Paper_2/HVI_D.xlsx"  # Replace with your file name
df = pd.read_excel(data_file, sheet_name="Sheet1")

# Prepare the data for linear regression
X = df['Adaptive Capacity Level'].values.reshape(-1, 1)  # Independent variable
y = df['HVI'].values  # Dependent variable

# Perform linear regression
model = LinearRegression()
model.fit(X, y)

# Generate predictions and calculate R²
y_pred = model.predict(X)
r_squared = model.score(X, y)

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(X, y, c='blue', alpha=0.6, label='Data points')

# Plot the regression line with R²
plt.plot(X, y_pred, color='red', linewidth=2, 
         label=f'Regression Line: y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}\n$R^2$ = {r_squared:.2f}')

# Labels and title
plt.xlabel('Adaptive Capacity')
plt.ylabel('HVI')
plt.legend(fontsize=13, loc='upper right')
plt.grid(True)

# Show the plot
plt.show()
