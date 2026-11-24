import time
import random

from lightning_detector import detect_lightning
from ai_prediction import predict_risk
from farmer_alert import send_alert


def run_vajrawatch():

    print("\n==============================")
    print("   VAJRAWATCH SAFETY SYSTEM")
    print("==============================")

    # Detect lightning distance
    distance = detect_lightning()

    # Simulate weather sensor readings
    humidity = random.randint(50, 100)
    wind_speed = random.randint(5, 40)

    print("\nWeather Readings")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind_speed, "km/h")

    # Predict risk level
    risk = predict_risk(distance, humidity, wind_speed)

    # Alert the farmer
    send_alert(risk)

    print("\nMonitoring cycle completed.")


if __name__ == "__main__":
    run_vajrawatch()
