# Real-time Temperature and Humidity Monitoring using Firebase and Matplotlib

## Overview
This project continuously fetches temperature and humidity data from a Firebase Realtime Database and visualizes the data using Matplotlib in real-time. The script updates the plots dynamically to reflect the latest sensor readings.

## Features
- Fetches temperature and humidity data from Firebase Realtime Database.
- Plots temperature and humidity in real-time.
- Displays only the last 20 data points for clarity.
- Updates every 2 seconds for near real-time visualization.
- Uses Matplotlib for graphical representation.

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install matplotlib firebase-admin
```

## Firebase Setup
1. Create a Firebase project on [Firebase Console](https://console.firebase.google.com/).
2. Set up a Realtime Database and get the database URL.
3. Download your Firebase Admin SDK JSON file and replace `esptest1-cfd44-firebase-adminsdk-fbsvc-db6b93ce01.json` in the script with the correct path.
4. Ensure your database structure contains `Sensor` with `Temp` and `Humid` values.

## Usage
1. Run the script:

```sh
python script.py
```

2. The script will continuously fetch data and update the plot every 2 seconds.

## Code Breakdown
- Initializes Firebase using Admin SDK.
- Retrieves sensor data from the `Sensor` reference in Firebase.
- Stores timestamps, temperature, and humidity values.
- Maintains only the last 20 entries for clarity.
- Updates the Matplotlib plot dynamically every 2 seconds.
