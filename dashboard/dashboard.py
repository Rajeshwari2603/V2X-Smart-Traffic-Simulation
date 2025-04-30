import os
import sys
import time
import tkinter as tk
from tkinter import StringVar

# SUMO setup
os.environ["SUMO_HOME"] = "C:/Program Files (x86)/Eclipse/Sumo"
tools = os.path.join(os.environ["SUMO_HOME"], "tools")
sys.path.append(tools)

try:
    import traci
except ImportError:
    print("❌ TraCI import failed")
    sys.exit(1)

sumo_binary = "sumo-gui"
sumo_config = "config/config.sumocfg"

# Start SUMO
traci.start([sumo_binary, "-c", sumo_config])
print("✅ SUMO Started")

# GUI setup
root = tk.Tk()
root.title("V2X Traffic Dashboard")

root.geometry("400x300")
root.resizable(False, False)

# UI Variables
vehicle_count = StringVar()
emergency_status = StringVar()
avg_speed = StringVar()
weather_status = StringVar()
alert_text = StringVar()

vehicle_count.set("0")
emergency_status.set("None")
avg_speed.set("0.0 m/s")
weather_status.set("Raining ☔")
alert_text.set("Running Normally ✅")

# UI Layout
tk.Label(root, text="🚦 V2X Traffic Simulation", font=("Arial", 16)).pack(pady=10)

tk.Label(root, textvariable=vehicle_count, font=("Arial", 14)).pack()
tk.Label(root, textvariable=emergency_status, font=("Arial", 14), fg="red").pack()
tk.Label(root, textvariable=avg_speed, font=("Arial", 14)).pack()
tk.Label(root, textvariable=weather_status, font=("Arial", 14), fg="blue").pack()
tk.Label(root, textvariable=alert_text, font=("Arial", 14), fg="orange").pack(pady=10)

# Update Loop
def update_dashboard():
    traci.simulationStep()
    vids = traci.vehicle.getIDList()
    emergency_vehicles = [v for v in vids if v.startswith("em")]
    normal_vehicles = [v for v in vids if not v.startswith("em")]

    # Update vehicle info
    vehicle_count.set(f"🚗 Vehicles: {len(vids)}")
    emergency_status.set(f"🚨 Emergency: {'YES' if emergency_vehicles else 'None'}")

    # Average speed
    speeds = [traci.vehicle.getSpeed(v) for v in normal_vehicles]
    avg = round(sum(speeds) / len(speeds), 2) if speeds else 0
    avg_speed.set(f"📉 Avg Speed: {avg} m/s")

    # Weather status (fixed to rain for now)
    weather_status.set("🌧️ Rain Active")

    # Alert
    if emergency_vehicles and avg < 1:
        alert_text.set("🚨 Emergency Stop Triggered!")
    elif avg < 2:
        alert_text.set("⚠️ Congestion Detected")
    else:
        alert_text.set("✅ Running Normally")

    # Schedule next update
    if traci.simulation.getMinExpectedNumber() > 0:
        root.after(500, update_dashboard)
    else:
        alert_text.set("✅ Simulation Finished")
        traci.close()

# Start loop
update_dashboard()
root.mainloop()
