# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:01:28 2026

@author: Admin
"""

#### Monte carlo simulation- uncertainty analysis
   
import geopandas as gpd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Load shapefile and summary
# -----------------------------
shapefile = r"D:/Dissertation writing/shape_file/gadm41_BGD_shp/gadm41_BGD_2.shp"
summary_file = os.path.join(out_dir, "MC_summary.xlsx")

gdf = gpd.read_file(shapefile)
summary = pd.read_excel(summary_file)

gdf = gdf.to_crs(epsg=32646)  # UTM
gdf = gdf.merge(summary, on="NAME_2", how="left")

# -----------------------------

# -----------------------------
# Function to fix map aspect
# -----------------------------
def fix_map_aspect(ax, gdf):
    # Get the bounding box of the geometries
    xmin, ymin, xmax, ymax = gdf.total_bounds
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect('auto')  # this now preserves true proportions

# -----------------------------
# Monte Carlo maps with 2-decimal legends
# -----------------------------
fig = plt.figure(figsize=(12, 12))

map_width = 0.40
map_height = 0.4
hspace = 0.05

legend_kwds = {"format": "%.2f", "shrink": 0.8}

# (a) Mean HVI
ax1 = fig.add_axes([0.05, 0.55, map_width, map_height])
gdf.plot(
    column="hvi_mean",
    cmap="OrRd",
    legend=True,
    legend_kwds=legend_kwds,
    ax=ax1,
    edgecolor="black",
    linewidth=0.3
)
ax1.set_title("(a)", fontsize=14)
ax1.set_axis_off()
fix_map_aspect(ax1, gdf)

# (b) CI Width
ax2 = fig.add_axes([0.05 + map_width + hspace, 0.55, map_width, map_height])
gdf.plot(
    column="hvi_ci_width",
    cmap="viridis",
    legend=True,
    legend_kwds=legend_kwds,
    ax=ax2,
    edgecolor="black",
    linewidth=0.3
)
ax2.set_title("(b)", fontsize=14)
ax2.set_axis_off()
fix_map_aspect(ax2, gdf)

# (c) Probability Top 25%
ax3 = fig.add_axes([(1 - map_width)/2, 0.05, map_width, map_height])
gdf.plot(
    column=f"prob_top{int(top_frac*100)}",
    cmap="RdYlBu",
    legend=True,
    legend_kwds=legend_kwds,
    ax=ax3,
    edgecolor="black",
    linewidth=0.3
)
ax3.set_title("(c)", fontsize=14)
ax3.set_axis_off()
fix_map_aspect(ax3, gdf)

plt.savefig(os.path.join(out_dir, "MC_maps_centered_fixed.png"),
            dpi=300, bbox_inches="tight")
plt.show()





