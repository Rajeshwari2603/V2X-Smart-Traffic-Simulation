import os
import sys
import time

# SUMO path setup
os.environ["SUMO_HOME"] = "C:/Program Files (x86)/Eclipse/Sumo"
tools = os.path.join(os.environ["SUMO_HOME"], "tools")
sys.path.append(tools)

try:
    import traci
except ImportError:
    print("❌ Could not import TraCI.")
    sys.exit(1)

sumo_binary = "sumo-gui"
sumo_config = "config/config.sumocfg"

def run():
    print("🚦 Starting SUMO...")
    traci.start([sumo_binary, "-c", sumo_config])

    rain_active = True  # Simulate that it's raining from start
    rain_alert_created = False

    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        vehicles = traci.vehicle.getIDList()

        for vid in vehicles:
            if vid.startswith("em"):
                print(f"🚨 Emergency vehicle: {vid}")
                for other in vehicles:
                    if other != vid:
                        traci.vehicle.setSpeed(other, 0)
            else:
                if rain_active:
                    traci.vehicle.setSpeed(vid, 5.0)  # slow due to rain
                else:
                    traci.vehicle.setSpeed(vid, 10.0)  # normal speed

        # 🔵 Add rain alert POI if not already shown
        if rain_active and not rain_alert_created:
            traci.polygon.add("rain_warning", shape=[(20,20), (22,20), (22,22), (20,22)],
                              color=(0, 0, 255, 255), fill=True, layer=1)
            print("🌧️ RAIN ALERT displayed!")
            rain_alert_created = True

        time.sleep(0.1)

    traci.close()
    print("✅ Simulation complete.")

if __name__ == "__main__":
    run()
