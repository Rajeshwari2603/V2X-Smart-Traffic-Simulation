import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import sys

# SUMO setup
os.environ["SUMO_HOME"] = "C:/Program Files (x86)/Eclipse/Sumo"
tools = os.path.join(os.environ["SUMO_HOME"], "tools")
sys.path.append(tools)

try:
    import traci
except ImportError:
    print("❌ Could not import TraCI")
    sys.exit(1)

sumo_binary = "sumo-gui"
sumo_config = "config/config.sumocfg"

# Start SUMO
traci.start([sumo_binary, "-c", sumo_config])
print("✅ SUMO Started")

speed_data = []
steps = []
emergency_markers = []

fig, ax = plt.subplots()

def update(frame):
    traci.simulationStep()
    veh_ids = traci.vehicle.getIDList()

    emergency_ids = [vid for vid in veh_ids if vid.startswith("em")]
    normal_ids = [vid for vid in veh_ids if not vid.startswith("em")]

    emergency_present = len(emergency_ids) > 0

    # Force vehicles to slow down due to rain
    for vid in normal_ids:
        traci.vehicle.setSpeedMode(vid, 0)  # Disable default speed control
        traci.vehicle.setSpeed(vid, 5.0)    # Rain speed default

    # 🚨 Stop all vehicles if emergency is present
    if emergency_present:
        print(f"🚨 Emergency Detected: {emergency_ids}")
        for vid in normal_ids:
            traci.vehicle.setSpeed(vid, 0.0)

    # Measure average speed (excluding emergency)
    speeds = [traci.vehicle.getSpeed(vid) for vid in normal_ids]
    avg_speed = sum(speeds) / len(speeds) if speeds else 0

    speed_data.append(avg_speed)
    steps.append(frame)

    ax.clear()
    ax.plot(steps, speed_data, color='blue', label='Avg Speed')

    if emergency_present and avg_speed < 1.0:
        emergency_markers.append((frame, avg_speed))

    for mark in emergency_markers:
        ax.scatter(mark[0], mark[1], color='red', s=40, label='Emergency Stop')

    ax.set_ylim(0, 15)
    ax.set_title("Live Avg Speed of Vehicles")
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Avg Speed (m/s)")
    ax.legend(loc="upper right")
    ax.grid(True)


ani = animation.FuncAnimation(fig, update, interval=1000)
plt.show()

# Save image
plt.savefig("speed_graph.png")
print("📸 Graph saved as speed_graph.png")

traci.close()
print("✅ Simulation done")