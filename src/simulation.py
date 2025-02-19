import time

class V2XSimulation:
    def __init__(self):
        print(" Initializing V2X Smart Traffic Simulation...")

    def simulate_traffic_density(self):
        print("\n Scenario: High Traffic Density")
        print(" Traffic congestion increasing...")
        
        print(" Network latency increasing due to more vehicles...")
        
        print(" Simulation completed: Traffic density impact analyzed.\n")

    def simulate_weather_conditions(self):
        print("\n Scenario: Adverse Weather Conditions")
        print(" Simulating heavy rain affecting V2X signals...")
        
        print(" Reduced visibility causing delays in vehicle communication...")
        
        print(" Simulation completed: Weather impact analyzed.\n")

    def simulate_emergency_vehicle_priority(self):
        print("\n Scenario: Emergency Vehicle Priority")
        print(" Detecting emergency vehicle in traffic...")
        
        print(" Giving priority by adjusting traffic signals...")
        
        print(" Simulation completed: Emergency vehicle priority system working.\n")

    def run(self):
        while True:
            print("\n Choose a scenario to simulate:")
            print("1️ High Traffic Density")
            print("2️ Adverse Weather Conditions")
            print("3️ Emergency Vehicle Priority")
            print("4️ Exit")
            choice = input("🔹 Enter the scenario number: ")

            if choice == "1":
                self.simulate_traffic_density()
            elif choice == "2":
                self.simulate_weather_conditions()
            elif choice == "3":
                self.simulate_emergency_vehicle_priority()
            elif choice == "4":
                print(" Exiting simulation.")
                break
            else:
                print(" Invalid choice. Please enter a valid number.")

# Run the simulation
if __name__ == "__main__":
    sim = V2XSimulation()
    sim.run()
