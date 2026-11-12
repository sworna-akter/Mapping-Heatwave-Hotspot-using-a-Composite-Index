# Mapping Heatwave Hotspots in Bangladesh

**Statistical and Spatial Analysis of a Composite Vulnerability Index**

## Project Overview

This research assesses heatwave vulnerability across all 64 districts of Bangladesh using a composite Heatwave Vulnerability Index (HVI). The index integrates three dimensions: **exposure, sensitivity, and adaptive capacity**.

The study examines the spatial distribution of heatwave vulnerability and identifies statistically significant clusters and hotspots to support geographically targeted climate adaptation planning.

## Research Objectives

- Develop a district-level composite Heatwave Vulnerability Index (HVI).
- Examine the spatial distribution of heatwave vulnerability across Bangladesh.
- Identify vulnerability clusters, spatial outliers, and hotspots.
- Investigate spatial variations in the relationships between HVI and its contributing factors.
- Evaluate the robustness and uncertainty of HVI rankings.

## Study Area

The study covers all 64 districts of Bangladesh across its eight administrative divisions.

## Data Sources

The research uses environmental, demographic, and socioeconomic indicators from:

- **MODIS:** Land Surface Temperature (LST), 2013–2022.
- **Bangladesh Bureau of Statistics (BBS):** Population and demographic and socioeconomic indicators (2011 and 2016).
- **Sentinel-2 / ESRI Living Atlas:** Vegetation, surface water, and built-up area information.
- **VIIRS / NASA:** Average nighttime light radiance.
- **LGED:** District administrative boundary shapefiles.

## Methodology

The analysis follows these main stages:

1. Data collection and preparation at district level.
2. Min–max normalisation of the selected indicators.
3. Construction of exposure, sensitivity, and adaptive capacity indices.
4. Calculation of the composite HVI.
5. District-level spatial mapping and statistical analysis.
6. Cluster and outlier analysis using Anselin Local Moran's I.
7. Hotspot analysis using Getis-Ord Gi*.
8. Geographically Weighted Regression (GWR).
9. Sensitivity analysis using alternative indicator-weighting scenarios.
10. Uncertainty assessment using Monte Carlo simulation.

### HVI Calculation

The composite index is calculated as:

**HVI = Exposure Index + Sensitivity Index − Adaptive Capacity Index**

## Key Findings

- Heatwave vulnerability varies considerably across Bangladesh.
- Central Bangladesh and the Dhaka peri-urban belt contain prominent high-vulnerability areas.
- Dhaka, Narayanganj, Gazipur, Manikganj, and Tangail emerge as important vulnerability hotspots.
- Exposure and sensitivity show positive relationships with HVI, while adaptive capacity has a protective, negative relationship.
- GWR reveals spatial variation in the relationships between vulnerability and its contributing factors.
- Sensitivity analysis indicates that district rankings remain broadly stable under alternative weighting scenarios.
- Monte Carlo simulation supports the stability of the major high-vulnerability areas under the tested uncertainty assumptions.

## Tools and Techniques

- Geographic Information Systems (GIS) and ArcGIS
- Min–max normalisation
- Composite index construction
- Anselin Local Moran's I
- Getis-Ord Gi*
- Geographically Weighted Regression (GWR)
- Spearman rank correlation
- Monte Carlo simulation

## Authors

- **Sworna Akter** (Lead researcher)– Conceptualisation, methodology, analysis, software, validation, and writing.

## Data Availability

The data used and/or analysed in this research are available from the corresponding author upon valid request. This repository shares research documentation and outputs that can be publicly distributed, subject to relevant data permissions.
