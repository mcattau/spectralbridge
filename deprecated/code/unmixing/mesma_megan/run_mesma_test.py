import numpy as np

from unmixing import ies_from_library

print("Test script started")

# Tiny fake spectral library:
# 6 spectra, 7 Landsat-like bands
spectral_library = np.array([
    [0.10, 0.12, 0.14, 0.18, 0.22, 0.24, 0.25],
    [0.11, 0.13, 0.15, 0.19, 0.23, 0.25, 0.26],
    [0.30, 0.28, 0.25, 0.20, 0.18, 0.16, 0.15],
    [0.31, 0.29, 0.26, 0.21, 0.19, 0.17, 0.16],
    [0.05, 0.06, 0.07, 0.30, 0.45, 0.40, 0.35],
    [0.06, 0.07, 0.08, 0.32, 0.47, 0.42, 0.36],
], dtype=np.float32)

results = ies_from_library(
    spectral_library=spectral_library,
    num_endmembers=4,
    initial_selection="dist_mean",
    stop_threshold=0.01
)

print("Selected endmember indices:")
print(results["indices"])

print("Max RMSE history:")
print(results["rmse_history"])

print("Mean RMSE history:")
print(results["avg_rmse_history"])

print("Stop index based on max RMSE:")
print(results["stop_max_idx"])

print("Stop index based on mean RMSE:")
print(results["stop_mean_idx"])

print("Test script finished")
