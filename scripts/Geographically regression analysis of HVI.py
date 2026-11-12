# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:04:28 2026

@author: Admin
"""


### Geographically regression analysis of HVI
import geopandas as gpd
import pandas as pd
import numpy as np
from mgwr.gwr import GWR
from mgwr.sel_bw import Sel_BW
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# -----------------------------
# Load data
# -----------------------------
shapefile_path = "D:/Dissertation writing/shape_file/gadm41_BGD_shp/gadm41_BGD_2.shp"
data_path = "D:/Dissertation writing/Paper_2/HVI_Data_Arcmap2.xlsx"

gdf = gpd.read_file(shapefile_path)
df = pd.read_excel(data_path, sheet_name="Sheet1")

# Merge shapefile and data
gdf = gdf.merge(df, on="NAME_2")

# -----------------------------
# Project to UTM (VERY IMPORTANT)
# -----------------------------
gdf = gdf.to_crs(epsg=32646)  # UTM Zone 46N (meters)

# -----------------------------
# Prepare variables
# -----------------------------
y = gdf['HVI'].values.reshape((-1, 1))
X = gdf[['Exposure Level', 'Sensitivity Level', 'Adaptive Capacity Level']].values

scaler = StandardScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y)

# -----------------------------
# Coordinates (centroids)
# -----------------------------
gdf['centroid'] = gdf.geometry.centroid
coords = np.column_stack((gdf.centroid.x, gdf.centroid.y))

# -----------------------------
# Bandwidth selection
# -----------------------------
bw = Sel_BW(coords, y, X).search()
print("Optimal bandwidth:", bw)

# -----------------------------
# Run GWR
# -----------------------------
gwr_model = GWR(coords, y, X, bw)
gwr_results = gwr_model.fit()
print(gwr_results.summary())

# -----------------------------
# Save local results
# -----------------------------
params = gwr_results.params
gdf['Intercept'] = params[:, 0]
gdf['Coef_Exposure'] = params[:, 1]
gdf['Coef_Sensitivity'] = params[:, 2]
gdf['Coef_Adaptive'] = params[:, 3]
gdf['Local_R2'] = gwr_results.localR2

# -----------------------------
# Segmented scale bar function
# -----------------------------
def add_figure_scalebar(fig, total_km=200, segment_km=50):
    ax = fig.add_axes([0.60, 0.05, 0.30, 0.04])  # bottom-right
    ax.axis('off')

    n_segments = int(total_km / segment_km)

    for i in range(n_segments):
        color = 'black' if i % 2 == 0 else 'white'
        ax.add_patch(
            plt.Rectangle(
                (i, 0), 1, 0.3,
                facecolor=color,
                edgecolor='black',
                linewidth=0.5
            )
        )

    ax.set_xlim(0, n_segments)
    ax.set_ylim(0, 1)

    # Labels
    labels = [0, 50, 100, 150, 200]
    for km in labels:
        ax.text(km / segment_km, -0.1, f"{km}",
                ha='center', va='top', fontsize=12)

    ax.text(n_segments / 2, -0.45, "Kilometers",
            ha='center', va='top', fontsize=14)


# -----------------------------
# Plot results
# -----------------------------
fig, axes = plt.subplots(2, 2, figsize=(12, 12))

plots = [
    ('Coef_Exposure', "(a)"),
    ('Coef_Sensitivity', "(b)"),
    ('Coef_Adaptive', "(c)"),
    ('Local_R2', "(d)")
]

for ax, (col, title) in zip(axes.flatten(), plots):

    gdf.plot(
        column=col,
        cmap='RdYlBu' if col != 'Local_R2' else 'viridis',
        legend=True,
        legend_kwds={'shrink': 0.6},
        ax=ax
    )

    ax.set_title(title, fontsize=13)
    ax.axis('off')
    ax.set_aspect('auto')

# --- Add ONE scale bar for entire figure ---
add_figure_scalebar(fig)

plt.subplots_adjust(wspace=0.15, hspace=0.15)
plt.show()


# -----------------------------
# Save results
# -----------------------------
# Drop extra geometry column before saving
gdf = gdf.drop(columns=['centroid'])

gdf.to_file(
    "D:/Dissertation writing/Paper_2/GWR_results.geojson",
    driver="GeoJSON"
)
