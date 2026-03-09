import sys
import pandas as pd
import folium
import requests

def parse_position(pos):
    pos = pos.replace("N", "").replace("E", " ")
    lat, lon = pos.split()
    return float(lat), float(lon)

def get_osrm_route(start, end):
    
    lon1, lat1 = start
    lon2, lat2 = end

    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{lon1},{lat1};{lon2},{lat2}"
        f"?overview=full&geometries=geojson"
    )

    r = requests.get(url)
    data = r.json()

    if "routes" not in data:
        raise RuntimeError("OSRM routing failed")

    return data["routes"][0]["geometry"]["coordinates"]

def main(csv_path):
    df = pd.read_csv(csv_path)

    if 'Position' not in df.columns:
        raise ValueError("Position column not found")

    df[['lat', 'lon']] = df['Position'].apply(
        lambda x: pd.Series(parse_position(x))
    )

    
    start = (df.iloc[0]['lon'], df.iloc[0]['lat'])
    end = (df.iloc[-1]['lon'], df.iloc[-1]['lat'])

    
    road_coords = get_osrm_route(start, end)

    
    road_coords = [(lat, lon) for lon, lat in road_coords]

    
    m = folium.Map(location=road_coords[0], zoom_start=11)

    folium.PolyLine(
        road_coords,
        color="blue",
        weight=5,
        opacity=0.9,
        tooltip="Road-following route (OSRM)"
    ).add_to(m)

    folium.Marker(
        road_coords[0],
        popup="Start",
        icon=folium.Icon(color="green", icon="play")
    ).add_to(m)

    folium.Marker(
        road_coords[-1],
        popup="End",
        icon=folium.Icon(color="red", icon="stop")
    ).add_to(m)

    m.save("route_marker.html")
    print("route_marker.html created")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python plot_polyline.py <position.csv>")
        sys.exit(1)

    main(sys.argv[1])


