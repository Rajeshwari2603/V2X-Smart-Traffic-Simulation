#  V2X Smart Traffic Simulation

## Overview

This project simulates a real-time smart traffic management system using **Vehicle-to-Everything (V2X)** communication at a busy 4-way intersection. The goal is to demonstrate how intelligent traffic systems can adapt to real-world conditions like emergency vehicle detection and weather changes to improve road safety and efficiency.

I built this project using **SUMO (Simulation of Urban MObility)** and **Python** via the **TraCI** interface. The system features:
- Adaptive traffic signal control
- Emergency vehicle prioritization
- Weather-aware traffic behavior
- A real-time dashboard to visualize and interact with the simulation

## My Contributions

- Designed and built the simulation environment using SUMO with a 4-way X-junction
- Implemented logic to detect emergency vehicles and override traffic lights to give them priority
- Created weather toggle functionality (rain) that slows down vehicles and triggers alerts
- Developed a Python-based dashboard using **Tkinter** to control rain, display alerts, and take simulation screenshots
- Integrated alert display and live traffic signal status viewer

## Key Features

- **Emergency Vehicle Behavior:** Other vehicles yield when an emergency vehicle is present
- **Weather Integration:** Rain condition slows down vehicles and raises alerts (planned integration with OpenWeatherMap API)
- **Live Dashboard:** GUI for real-time traffic state monitoring and simulation control
- **Speed Monitoring:** Generates and visualizes vehicle speed graphs
