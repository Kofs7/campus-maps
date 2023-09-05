"""Binary to find the geolocation of a building or road."""

import mapbox
import json
import os

_ACCESS_TOKEN = "pk.eyJ1Ijoia29mc3MiLCJhIjoiY2xtM3Nhd2VxMmw3NDNlcDM2cmNjMGpxbiJ9.Y7joTjrxLia56pqe46palA"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "locations.json")
    # Initialize the Mapbox Geocoder with your access token
    geocoder = mapbox.Geocoder(access_token=_ACCESS_TOKEN)

    with open(file_path) as f:
        data = json.load(f)
    for name, info in data.items():
        full_name = info["Full name"]
        if info["Location"] is not None:
            location = info["Location"]
        else:
            location = full_name
        # Perform geocoding
        response = geocoder.forward(f"{location}, Washington, DC")

        # Extract latitude and longitude
        first_feature = response.json()["features"][0]
        coordinates = first_feature["geometry"]["coordinates"]
        latitude, longitude = coordinates

        print(
            f"Name: {name} | Full name: {full_name} | Latitude: {latitude}, Longitude: {longitude}\n"
        )


if __name__ == "__main__":
    main()
