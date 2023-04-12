#Import required libraries
import paho.mqtt.client as mqtt
import random
import time
import datetime
import csv


# MQTT broker address and port and topic
ACCESS_TOKEN_1='1qntU93Qh1Eqs39uN2Eg'
ACCESS_TOKEN_2='7NZGPA9yJ7GYhZpG5SwY'
broker_address = "demo.thingsboard.io"
broker_port = 1883
topic = "v1/devices/me/telemetry"

# Virtual Enviornmental station 1 function
def get_sensor_data_station_1():
    data = {}
    data['station_Id'] = 1
    data['Temperature'] = round(random.uniform(-50, 50), 2)
    data['Humidity'] = round(random.uniform(0, 100), 2)
    data['CO2'] = round(random.uniform(300, 2000), 2)
    data['Rain_Height'] = round(random.uniform(0, 50), 2)
    data['Wind_Direction'] = round(random.uniform(0, 360), 2)
    data['Wind_Intensity'] = round(random.uniform(0, 100), 2)
    return data

# Virtual Enviornmental station 2 function
def get_sensor_data_station_2():
    data = {}
    data['station_Id'] = 2
    data['Temperature'] = round(random.uniform(-50, 50), 2)
    data['Humidity'] = round(random.uniform(0, 100), 2)
    data['CO2'] = round(random.uniform(300, 2000), 2)
    data['Rain_Height'] = round(random.uniform(0, 50), 2)
    data['Wind_Direction'] = round(random.uniform(0, 360), 2)
    data['Wind_Intensity'] = round(random.uniform(0, 100), 2)
    return data

# Connect to MQTT broker
client1 = mqtt.Client()   #create client MQTT object to send data to station 1
client2 = mqtt.Client()   #create client MQTT object to send data to station 1
client1.username_pw_set(ACCESS_TOKEN_1)   #access token from thingsboard device station 1
client2.username_pw_set(ACCESS_TOKEN_2)   #access token from thingsboard device station 2
client1.connect(broker_address , broker_port , keepalive=60)   #establish connection
client2.connect(broker_address , broker_port , keepalive=60)   #establish connection

# Get the current time
current_time = datetime.datetime.now()

# Calculate the time five hours from now
target_time = current_time + datetime.timedelta(minutes=1)

# Convert target time to timestamp
target_timestamp = target_time.timestamp()

# Create a csv file to store data for reference
with open('sensor_data.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Station Id','Temperature', 'Humidity', 'CO2', 'Rain_Height', 'Wind_Direction', 'Wind_Intensity','Time_Stamp'])

print("Timer Started at: ", current_time)

# Publish sensor data every 5 seconds until target time is reached 
while time.time() < target_timestamp:
    station1 = get_sensor_data_station_1()
    station2 = get_sensor_data_station_2()
    client1.publish(topic, str(station1))
    client2.publish(topic, str(station2))
    # open csv file in append mode to store sensor data
    with open('sensor_data.csv', mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([station1['station_Id'],station1['Temperature'],station1['Humidity'],station1['CO2'], station1['Rain_Height'],station1['Wind_Direction'],station1['Wind_Intensity'],datetime.datetime.now()])
        writer.writerow([station2['station_Id'],station2['Temperature'], station2['Humidity'], station2['CO2'], station2['Rain_Height'], station2['Wind_Direction'],station2['Wind_Intensity'],datetime.datetime.now()])

    time.sleep(5)

print("Finished at: ", datetime.datetime.now())