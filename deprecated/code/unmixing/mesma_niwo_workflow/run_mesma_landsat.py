import numpy as np
from mesma_core import MesmaModels, MesmaCore

# load image cube
image = np.load("landsat_niwo_20200702_cube.npy")

# load library
library = np.load("library_oli_6band.npy")

# load class labels
class_list = np.load("class_list_oli.npy", allow_pickle=True)

print("Image shape:")
print(image.shape)

print("\nLibrary shape:")
print(library.shape)

print("\nClass list shape:")
print(class_list.shape)

# build MESMA models
models_builder = MesmaModels()

models_builder.setup(class_list)

print("\nMESMA summary:")
print(models_builder.summary())

# build lookup table for MESMA
look_up_table = models_builder.return_look_up_table()
em_per_class = models_builder.em_per_class

# initialize MESMA
mesma = MesmaCore(n_cores=1)

# execute MESMA
models, fractions, rmse, residuals = mesma.execute(
    image=image,
    library=library,
    look_up_table=look_up_table,
    em_per_class=em_per_class,
    residual_image=False
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

# save outputs
np.save("fractions.npy", fractions)
np.save("rmse.npy", rmse)
np.save("models.npy", models)

print("\nSaved:")
print("fractions.npy")
print("rmse.npy")
print("models.npy")
