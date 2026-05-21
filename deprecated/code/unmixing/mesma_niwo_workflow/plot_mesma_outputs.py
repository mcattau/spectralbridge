import numpy as np
import matplotlib.pyplot as plt

fractions = np.load("mesma_fractions_landsat.npy")
rmse = np.load("mesma_rmse_landsat.npy")

classes = [
    "deciduous",
    "evergreen",
    "herbaceous",
    "non_vegetated_dead",
    "woody_shrub",
    "shade"
]

print("Fractions shape:", fractions.shape)
print("RMSE shape:", rmse.shape)

for i, name in enumerate(classes):
    arr = fractions[i]

    plt.figure(figsize=(5, 8))
    plt.imshow(arr, vmin=0, vmax=1)
    plt.colorbar(label="Fraction")
    plt.title(f"MESMA fraction: {name}")
    plt.tight_layout()

    out = f"mesma_fraction_{name}.png"
    plt.savefig(out, dpi=200)
    plt.close()

    print(out, "min=", np.nanmin(arr), "max=", np.nanmax(arr))

plt.figure(figsize=(5, 8))
plt.imshow(rmse)
plt.colorbar(label="RMSE")
plt.title("MESMA RMSE")
plt.tight_layout()
plt.savefig("mesma_rmse.png", dpi=200)
plt.close()

print("mesma_rmse.png", "min=", np.nanmin(rmse), "max=", np.nanmax(rmse))
