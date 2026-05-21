from pystac_client import Client
import planetary_computer
import rasterio
from rasterio.windows import Window
import numpy as np

target_id = "LC08_L2SP_034032_20200702_02_T1"

bands = ["blue", "green", "red", "nir08", "swir16", "swir22"]

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1"
)

search = catalog.search(
    collections=["landsat-c2-l2"],
    ids=[target_id],
)

item = planetary_computer.sign(list(search.items())[0])

for band in bands:
    href = item.assets[band].href

    with rasterio.open(href) as src:
        print("\nBand:", band)
        print("Shape:", src.height, src.width)
        print("CRS:", src.crs)
        print("dtype:", src.dtypes[0])
        print("nodata:", src.nodata)

        # read small 100 x 100 window from center
        row_start = src.height // 2
        col_start = src.width // 2

        arr = src.read(
            1,
            window=Window(col_start, row_start, 100, 100)
        ).astype("float32")

        arr[arr == src.nodata] = np.nan

        print("Raw min:", np.nanmin(arr))
        print("Raw max:", np.nanmax(arr))

        # Landsat Collection 2 Level 2 SR scale/offset
        refl = arr * 0.0000275 - 0.2

        print("Reflectance min:", np.nanmin(refl))
        print("Reflectance max:", np.nanmax(refl))
