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

  ### Real-Time Dashboard  
Displays live traffic status, emergency detection, rain toggle, and simulation alerts.
![dashboard-status](https://github.com/user-attachments/assets/504e9fb0-4bbb-4201-a755-6a01e579c2c1)


### Vehicle Speed Monitoring  
**Graph showing average speed and emergency stops over time.**
![speed-graph](https://github.com/user-attachments/assets/5780ec8c-9ff8-41b0-987c-e2759f91c587)

### SUMO Simulation View  
SUMO visualization of traffic flow through an X-junction.  
 **Green vehicle represents the emergency vehicle, other vehicles yield to it.**![sumo-simulation](https://github.com/user-attachments/assets/1595de90-30f5-4ee4-ab4d-9fec5c8fd6a6)

 ##  Sprint Summary

| Sprint   | Goal                                | Key Output                                                  
|----------|----------------------------------   |----------------------------------------
| Sprint 1 | Set up basic simulation with SUMO   | 4-way junction, vehicle routing,configuration 
                                                   files       
| Sprint 2 | Emergency vehicle logic             | Emergency vehicle priority and stopping 
                                                   normal traffic     
| Sprint 3 | Rain condition handling             | Slows down vehicles, triggers dashboard alert              
| Sprint 4 | Interactive dashboard               | GUI with live status, alert display, 
                                                   screenshot functionality

---

## 🧩 Task Overview

| Task / User Story                             | Status  | Notes                                                                 
|-----------------------------------------------|---------|-----------------------------------
| Vehicles yield to emergency vehicles          | Done    | Used TraCI logic to identify 
                                                            emergency and stop other vehicles         
| Rain triggers speed reduction + alert         | Done    | Handled in `traffic_control.py`, 
                                                            shown in dashboard                    
| Dashboard displays simulation status          | Done    | Built using Tkinter, shows vehicles, 
                                                            alerts, signal state              
| Snapshot of current traffic simulation        | Done    | Tkinter "Screenshot" button 
                                                            implemented                                
| Live signal phase display                     |  Done   | Signal status displayed live in GUI                                    


