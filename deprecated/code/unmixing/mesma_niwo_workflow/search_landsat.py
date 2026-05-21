from pystac_client import Client
import planetary_computer

lon = -105.49
lat = 40.03

catalog = Client.open("https://planetarycomputer.microsoft.com/api/stac/v1")

search = catalog.search(
    collections=["landsat-c2-l2"],
    intersects={"type": "Point", "coordinates": [lon, lat]},
    datetime="2020-06-01/2020-09-01",
    query={"eo:cloud_cover": {"lt": 10}},
)

items = list(search.items())
print(f"Found {len(items)} scenes\n")

for item in items[:10]:
    item = planetary_computer.sign(item)
    print("ID:", item.id)
    print("Date:", item.datetime)
    print("Cloud cover:", item.properties["eo:cloud_cover"])
    print("---")
