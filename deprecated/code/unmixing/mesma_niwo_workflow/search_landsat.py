from pystac_client import Client
import planetary_computer

# NIWO approximate center
lon = -105.49
lat = 40.03

catalog = Client.open(
    "https://planetarycomputer.microsoft.com/api/stac/v1"
)

search = catalog.search(
    collections=["landsat-c2-l2"],
    intersects={
        "type": "Point",
        "coordinates": [lon, lat],
    },
    datetime="2020-06-01/2020-09-01",
    query={
        "eo:cloud_cover": {"lt": 10}
    }
)

items = list(search.items())

print(f"Found {len(items)} scenes\n")

for item in items[:10]:

    signed_item = planetary_computer.sign(item)

    print("ID:", signed_item.id)
    print("Date:", signed_item.datetime)
    print("Cloud cover:", signed_item.properties["eo:cloud_cover"])
    print("---")
