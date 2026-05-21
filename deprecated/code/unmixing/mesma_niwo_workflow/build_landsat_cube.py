import rasterio
from rasterio.windows import from_bounds
from rasterio.warp import transform_bounds
from pystac_client import Client
import planetary_computer
import rasterio
from rasterio.windows import from_bounds
import numpy as np

target_id = "LC08_L2SP_034032_20200702_02_T1"

bands = ["blue", "green", "red", "nir08", "swir16", "swir22"]

# NIWO approximate lon/lat bounding box from library
lon_min, lat_min = -105.496, 40.006
lon_max, lat_max = -105.492, 40.058

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1"
)

search = catalog.search(
    collections=["landsat-c2-l2"],
    ids=[target_id],
)

item = planetary_computer.sign(list(search.items())[0])

arrays = []

for band in bands:
    href = item.assets[band].href

    with rasterio.open(href) as src:
        # Convert lon/lat bounds to raster CRS
        bounds = transform_bounds(
            "EPSG:4326",
            src.crs,
            lon_min,
            lat_min,
            lon_max,
            lat_max
        )

        window = from_bounds(*bounds, transform=src.transform)

        arr = src.read(1, window=window).astype("float32")

        arr[arr == src.nodata] = np.nan

        # Landsat Collection 2 Level 2 scale/offset
        arr = arr * 0.0000275 - 0.2

        # MESMA expects 0–1 reflectance
        arr[arr < 0] = 0
        arr[arr > 1] = np.nan

        arrays.append(arr)

image = np.stack(arrays, axis=0)

print("Image cube shape:")
print(image.shape)

print("\nBand min/max:")
for band, arr in zip(bands, image):
    print(band, np.nanmin(arr), np.nanmax(arr))

np.save("landsat_niwo_20200702_cube.npy", image)

print("\nSaved landsat_niwo_20200702_cube.npy")
