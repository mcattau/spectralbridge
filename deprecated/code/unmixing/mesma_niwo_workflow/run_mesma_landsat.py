import numpy as np
from mesma_core import MesmaModels, MesmaCore

image = np.load("landsat_niwo_20200702_cube.npy")
library = np.load("library_oli_6band.npy")
class_list = np.load("class_list_oli.npy", allow_pickle=True)

print("Image shape:")
print(image.shape)

print("\nLibrary shape:")
print(library.shape)

print("\nClass list shape:")
print(class_list.shape)

models_builder = MesmaModels()
models_builder.setup(class_list)

print("\nMESMA summary:")
print(models_builder.summary())

look_up_table = models_builder.return_look_up_table()
em_per_class = models_builder.em_per_class

mesma = MesmaCore(n_cores=1)

models, fractions, rmse, residuals = mesma.execute(
    image=image,
    library=library,
    look_up_table=look_up_table,
    em_per_class=em_per_class,
    residual_image=False,
)

print("\nFinished MESMA")

print("\nModels shape:")
print(models.shape)

print("\nFractions shape:")
print(fractions.shape)

print("\nRMSE shape:")
print(rmse.shape)

print("\nFraction ranges:")
for i in range(fractions.shape[0]):
    print(i, np.nanmin(fractions[i]), np.nanmax(fractions[i]))

print("\nRMSE range:")
print(np.nanmin(rmse), np.nanmax(rmse))

np.save("mesma_models_landsat.npy", models)
np.save("mesma_fractions_landsat.npy", fractions)
np.save("mesma_rmse_landsat.npy", rmse)

print("\nSaved:")
print("mesma_models_landsat.npy")
print("mesma_fractions_landsat.npy")
print("mesma_rmse_landsat.npy")
