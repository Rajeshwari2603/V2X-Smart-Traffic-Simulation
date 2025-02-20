import pandas as pd

class DataProcessing:
    def __init__(self):
        self.traffic_data = None
        self.weather_data = []
    
    def load_traffic_data(self, file_path):
        """Read traffic data from a CSV file."""
        try:
            self.traffic_data = pd.read_csv(file_path)
            print("Traffic data loaded successfully!")
        except Exception as e:
            print(f"Error loading CSV file: {e}")
    
    def process_traffic_data(self):
        """Process and clean traffic data (e.g., extracting relevant columns)."""
        if self.traffic_data is not None:
            # Example: Extracting relevant columns for simulation (e.g., time and traffic volume)
            self.traffic_data = self.traffic_data[['date_time', 'traffic_volume']]  # Adjust based on your CSV columns
            self.traffic_data['date_time'] = pd.to_datetime(self.traffic_data['date_time'])
            print("Processed Traffic Data:", self.traffic_data.head())
        else:
            print("No traffic data loaded to process.")
    
    def generate_weather_data(self):
        """Simulate weather conditions for each time period"""
        weather_conditions = ['Clear', 'Cloudy', 'Rain', 'Storm']
        self.weather_data = {time: random.choice(weather_conditions) for time in ['Morning', 'Afternoon', 'Evening', 'Night']}
        print("Generated Weather Data:", self.weather_data)

    def process_data(self, file_path):
        """Process and clean both traffic and weather data."""
        self.load_traffic_data(file_path)
        self.process_traffic_data()
        self.generate_weather_data()

        return self.traffic_data, self.weather_data

# Testing the data processing
if __name__ == "__main__":
    data_processor = DataProcessing()
    file_path = "C:\\Users\\rajes\\V2X-Smart-Traffic-Simulation\\data\\Metro_Interstate_Traffic_Volume.csv"


    traffic_data, weather_data = data_processor.process_data(file_path)
    print("Processed Traffic Data:", traffic_data)
    print("Processed Weather Data:", weather_data)
