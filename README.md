# Cloud-based-IoT-System-for-Collecting-Data-from-Virtual-Sensors

This project aims to demonstrate how to create a cloud-based IoT system that collects data from virtual sensors using the MQTT protocol. 
The system uses Python programming language to simulate virtual environmental stations and sends data to a cloud-based backend using MQTT. 
The backend used in this project is Thingsboard.

## Getting Started 

### Prerequisites
To run this project, you will need the following:

1. Python 3.x installed on your computer
2. Paho MQTT library
3. Access to a Thingsboard account

### Installing

1. Clone this repository - git clone https://github.com/ChaitanyaA96/Cloud-based-IoT-System-for-Collecting-Data-from-Virtual-Sensors.git

2. Install Paho - pip install paho-mqtt

3. Run project by running following script - IOT_Cloud_based_system_virtual_sensors.py

4. Log in to your Thingsboard account and navigate to the Devices section.

5. Create 2 devices -  for each environmental station

6. Create dashboard - As per your visualization requirement.

### Features

The project includes the following features:

1. Simulated virtual environmental stations that generate a set of random virtual sensor values for temperature, humidity, CO2 sensor, rain height, wind      direction, and wind intensity.
2. MQTT protocol to connect the virtual sensors to a cloud-based backend.
3. Thingsboard IoT as the cloud-based backend.
4. Data visualization using Thingsboard dashboards to display the most recent sensor data values as well as sensor data values received in the previous        five hours.

### Future Improvements
The project can be expanded further by incorporating additional virtual sensors and advanced analytics to gain insights from the collected data.

### Acknowledgments
[Paho MQTT](https://www.eclipse.org/paho/index.php)
[Thingsboard](https://thingsboard.io/)
[Python](https://www.python.org/)

