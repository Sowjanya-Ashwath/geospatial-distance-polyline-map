import sys
import pandas as pd
from datetime import datetime, timedelta


START_LAT = 28.9169
START_LON = 77.1152
END_LAT = 28.0980
END_LON = 77.3248

START_TIME = datetime.strptime("2024-01-28 07:00:00", "%Y-%m-%d %H:%M:%S")

def parse_position(pos):
    pos = pos.replace("N", "").replace("E", " ")
    lat, lon = pos.split()
    return float(lat), float(lon)

def format_position(lat, lon):
    return f"N{lat:.6f}E{lon:.6f}"

def main(csv_path):
    df = pd.read_csv(csv_path)
    df.columns = df.columns.str.strip()

    
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    if 'Position' not in df.columns:
        raise ValueError("Position column not found")

    
    df[['lat', 'lon']] = df['Position'].apply(
        lambda x: pd.Series(parse_position(x))
    )

    
    df_sorted = df.sort_values(
        by=['lat', 'lon'],
        ascending=[False, True]
    ).reset_index(drop=True)

    
    positions = (
        [format_position(START_LAT, START_LON)]
        + df_sorted['Position'].tolist()
        + [format_position(END_LAT, END_LON)]
    )

    
    times = [
        START_TIME + timedelta(seconds=i)
        for i in range(len(positions))
    ]

    df_final = pd.DataFrame({
        'Position': positions,
        'Time': times
    })

    df_final.to_csv("position.csv", index=False)
    print("position.csv created")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python correction.py <position.csv>")
        sys.exit(1)

    main(sys.argv[1])

