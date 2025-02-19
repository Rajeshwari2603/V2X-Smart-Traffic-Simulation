import time
from security import SecureV2XCommunication

class V2XSimulation:
    def __init__(self):
        print(" Initializing V2X Smart Traffic Simulation...")
        self.secure_comm = SecureV2XCommunication()  # Initialize encryption

    def simulate_traffic_density(self):
        print("\n Scenario: High Traffic Density")
        message = "High traffic detected. Possible congestion ahead."
        encrypted_msg = self.secure_comm.encrypt_message(message)
        print(f" Encrypted Message Sent: {encrypted_msg}")
        time.sleep(1)
        decrypted_msg = self.secure_comm.decrypt_message(encrypted_msg)
        print(f" Decrypted Message Received: {decrypted_msg}\n")

    def simulate_weather_conditions(self):
        print("\n Scenario: Adverse Weather Conditions")
        message = "Severe weather detected. Adjusting speed limits."
        encrypted_msg = self.secure_comm.encrypt_message(message)
        print(f" Encrypted Message Sent: {encrypted_msg}")
        time.sleep(1)
        decrypted_msg = self.secure_comm.decrypt_message(encrypted_msg)
        print(f" Decrypted Message Received: {decrypted_msg}\n")

    def simulate_emergency_vehicle_priority(self):
        print("\n Scenario: Emergency Vehicle Priority")
        message = "Emergency vehicle detected. Clearing path."
        encrypted_msg = self.secure_comm.encrypt_message(message)
        print(f" Encrypted Message Sent: {encrypted_msg}")
        time.sleep(1)
        decrypted_msg = self.secure_comm.decrypt_message(encrypted_msg)
        print(f" Decrypted Message Received: {decrypted_msg}\n")

    def run(self):
        while True:
            print("\n🚦 Choose a scenario to simulate:")
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
