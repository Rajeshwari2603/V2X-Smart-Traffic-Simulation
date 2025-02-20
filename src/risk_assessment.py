import numpy as np
from sklearn.tree import DecisionTreeClassifier

class TrafficRiskAssessment:
    def __init__(self):
        self.data = [
            [60, 5], [80, 7], [40, 3], [90, 8], [50, 4], [70, 6]
        ]
        self.labels = ['Low', 'Medium', 'Low', 'High', 'Low', 'Medium']
        self.model = DecisionTreeClassifier()
        self.model.fit(self.data, self.labels)

    def assess_risk(self, traffic_density, weather_severity):
        prediction = self.model.predict([[traffic_density, weather_severity]])
        print(f"Prediction input: Traffic Density={traffic_density}, Weather Severity={weather_severity}")
        print(f"Prediction result: {prediction[0]}")
        return prediction[0]

if __name__ == "__main__":
    risk_assessment = TrafficRiskAssessment()
    traffic_density = 75
    weather_severity = 6
    risk_level = risk_assessment.assess_risk(traffic_density, weather_severity)
    print(f"Traffic Density: {traffic_density}, Weather Severity: {weather_severity}")
    print(f"Predicted Risk Level: {risk_level}")
