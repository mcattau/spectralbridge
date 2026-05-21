import numpy as np

library = np.load("library_oli.npy")

print("Original shape:")
print(library.shape)

# remove coastal band (first band)
library_6 = library[1:, :]

print("\n6-band shape:")
print(library_6.shape)

np.save("library_oli_6band.npy", library_6)

print("\nSaved library_oli_6band.npy")
