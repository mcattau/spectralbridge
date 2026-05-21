from pystac_client import Client
import planetary_computer

target_id = "LC08_L2SP_034032_20200702_02_T1"

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1"
)

search = catalog.search(
    collections=["landsat-c2-l2"],
    ids=[target_id],
)

items = list(search.items())

print("Items found:", len(items))

item = planetary_computer.sign(items[0])

print("ID:", item.id)
print("Date:", item.datetime)
print("Cloud cover:", item.properties.get("eo:cloud_cover"))

print("\nAssets:")
for key in item.assets.keys():
    print(key)
