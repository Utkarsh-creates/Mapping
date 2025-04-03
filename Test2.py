import matplotlib.pyplot as plt
import datetime
import time
import firebase_admin
from firebase_admin import credentials, db

# Load Firebase credentials and initialize app
cred = credentials.Certificate("esptest1-cfd44-firebase-adminsdk-fbsvc-db6b93ce01.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://esptest1-cfd44-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

# Reference to Firebase
ref = db.reference("Sensor")

# Initialize data lists
time_values = []
temp_values = []
humid_values = []

# Create figure and axes for two plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Continuous Loop for Live Updates
while True:
    data = ref.get()
    
    if data:
        current_time = datetime.datetime.now()
        temperature = data.get("Temp", None)
        humidity = data.get("Humid", None)
        
        # Store data
        time_values.append(current_time)
        temp_values.append(temperature)
        humid_values.append(humidity)

        # Keep only the last 20 points
        if len(time_values) > 20:
            time_values.pop(0)
            temp_values.pop(0)
            humid_values.pop(0)

        # Clear previous plots
        ax1.clear()
        ax2.clear()

        # Temperature Plot
        ax1.plot(time_values, temp_values, marker='o', linestyle='-', color='r', label="Temperature (°C)")
        ax1.set_title("Temperature vs Time")
        ax1.set_ylabel("Temperature (°C)")
        ax1.set_xlabel("Time")
        ax1.legend()
        ax1.grid(True)

        # Humidity Plot
        ax2.plot(time_values, humid_values, marker='s', linestyle='-', color='b', label="Humidity (%)")
        ax2.set_title("Humidity vs Time")
        ax2.set_ylabel("Humidity (%)")
        ax2.set_xlabel("Time")
        ax2.legend()
        ax2.grid(True)

        # Rotate x-axis labels for readability
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Show and update plot
        plt.pause(2)  # Pause for 2 seconds before the next update

