# Geospatial Distance Calculation and Polyline Map Visualization

## Project Overview

This project processes geographic coordinate data, converts encoded coordinates back to their original format, calculates the distance between sequential points, and visualizes the route on an interactive map using a polyline.

The goal of this project is to demonstrate geospatial data processing, distance computation, and map-based visualization using Python.

---

## Features

* Convert modified or encoded coordinate values into the correct latitude and longitude format
* Calculate distance between coordinates using the Haversine formula
* Compute the total route distance
* Generate an interactive map with a polyline representing the route
* Visualize geographic data using Python mapping libraries

---

## Technologies Used

* Python
* Pandas
* Folium
* NumPy

---


---

## Workflow

### 1. Coordinate Conversion

The coordinate data is initially stored in a modified format.
This step converts the coordinates into valid latitude and longitude values.

Example transformation:

```
Encoded Format → Original Format
123456 → 12.3456
987654 → 98.7654
```

---

### 2. Distance Calculation

The distance between consecutive coordinates is calculated using the **Haversine formula**, which computes the shortest distance between two points on the Earth’s surface.

This allows calculation of:

* distance between two points
* total route distance

---

### 3. Polyline Map Visualization

The coordinates are plotted on an interactive map using the **Folium library**.

A polyline connects the sequence of coordinates to represent the route taken.

The final map is saved as:

```
route_map.html
```

---

## How to Run the Project

### Install dependencies

```
pip install -r requirements.txt
```

### Run the script

```
python plot_polyline.py - To get the map
python distance_measured.py - To get the total distance 
```

The generated map will be saved in the `output` folder.

---

## Output

The project generates an interactive map showing the path between coordinates.

Example output:

![Polyline Map](images/polyline_map.png)

---

## Key Concepts Demonstrated

* Geospatial data processing
* Coordinate transformation
* Distance calculation using Haversine formula
* Route visualization using Python mapping tools
* Dat
