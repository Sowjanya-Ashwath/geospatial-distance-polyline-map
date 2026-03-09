import sys
import pandas as pd
import requests

def parse_position(pos):
    pos = pos.replace("N", "").replace("E", " ")
    lat, lon = pos.split()
    return float(lat), float(lon)

def osrm_distance(start, end):
    lon1, lat1 = start
    lon2, lat2 = end

    url = (
        f"http://router.project-osrm.org/route/v1/driving/"
        f"{lon1},{lat1};{lon2},{lat2}"
        f"?overview=false"
    )

    r = requests.get(url)
    data = r.json()

    if "routes" not in data:
        raise RuntimeError("OSRM routing failed")

    # distance is in meters
    return data["routes"][0]["distance"] / 1000

def main(csv_path):
    df = pd.read_csv(csv_path)

    if 'Position' not in df.columns:
        raise ValueError("Position column not found")

    # Extract lat/lon
    df[['lat', 'lon']] = df['Position'].apply(
        lambda x: pd.Series(parse_position(x))
    )

    # Start & End points
    start = (df.iloc[0]['lon'], df.iloc[0]['lat'])
    end = (df.iloc[-1]['lon'], df.iloc[-1]['lat'])

    distance_km = osrm_distance(start, end)

    print(f"Toatal distance travelled: {distance_km:.2f} km")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python distance_measured.py <position.csv>")
        sys.exit(1)

    main(sys.argv[1])



