🔍 Crime Data Analysis using Hadoop & Interactive Dashboard


📑 Table of Contents

1. [📘 Project Overview](#-project-overview)
2. [🎯 Key Features](#-key-features)
3. [🛠️ Tech Stack](#️-tech-stack)
4. [📂 Project Structure](#-project-structure)
5. [🚀 How to Run](#-how-to-run)
6. [📈 Hadoop MapReduce Workflow](#-hadoop-mapreduce-workflow)
7. [🧠 Insights & Results](#-insights--results)
8. [📄 License](#-license)

---

📘 Project Overview

A powerful Crime analytics platform that processes large-scale crime datasets using Hadoop MapReduce and visualizes insights using a web dashboard with charts and maps.

This project enables:
✅ Crime pattern analysis  
✅ Hotspot detection  
✅ User-friendly visualization  

---

🎯 Key Features

- ✅ Hadoop MapReduce processing for large crime datasets  
- ✅ Crime frequency analysis by type and location  
- ✅ Interactive Map showing crime hotspots  
- ✅ Modern dashboard using Chart.js & Leaflet.js  
- ✅ Scalable data pipeline  
- ✅ Clean UI for report visualization  

---

🛠️ Tech Stack

| Layer | Technologies Used |
|-------|------------------|
| Big Data Processing | Hadoop, HDFS, MapReduce, Python |
| Frontend Dashboard | HTML, CSS, Chart.js, Leaflet.js |
| Data Format | CSV Geographic Data |

---

📂 Project Structure

Crime-Data-Analysis/
│
├── README.md
├── dashboard.html
│
├── input/
│ └── crimes.csv
│
├── screenshots/ ← (Add your screenshots here)
│ ├── dashboard_graph.png
│ ├── crime_map.png
│
├── mapreduce/
│ ├── mapper.py
│ └── reducer.py
│
└── output/
├── crime_type_counts.csv
└── crime_locations.csv


---

How to Run

Step 1: Upload Dataset to HDFS
```bash
hdfs dfs -mkdir /crime_input
hdfs dfs -put input/crimes.csv /crime_input

Step 2: Run Hadoop Streaming Job
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /crime_input/crimes.csv \
-output /crime_output \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py"

Step 3: Retrieve Output
hdfs dfs -get /crime_output output/

Step 4: Open Web Dashboard
python3 -m http.server 8000
# Then open browser:
# http://localhost:8000/dashboard.html

Hadoop MapReduce Workflow

Dataset (crimes.csv)
        ⬇
Mapper.py → Extracts Crime Type & Location
        ⬇
Reducer.py → Counts Frequency & Groups Data
        ⬇
CSV Results
        ⬇
Interactive Dashboard Visualizations

Insights & Results

🔹 Theft, Battery, and Assault are the most common crime categories

🔹 Crime hotspots cluster in central & south regions of the city

🔹 Mapping with masked addresses protects sensitive details while showing patterns

License

This project is licensed under the MIT License.

Developed by: Dhiksha C G
