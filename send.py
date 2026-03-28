import requests
import random
import time

# Your Firebase URL (must end with /)
FIREBASE_URL = "https://smartsocket1-8add1-default-rtdb.firebaseio.com/"

while True:
    data = {
        "Bill": random.randint(100, 1000),
        "Status": random.choice(["ON", "OFF"]),
        "Unit": random.randint(1, 100)
    }

    response = requests.patch(FIREBASE_URL + ".json", json=data)

    print("Updated:", data)
    time.sleep(1)   # updates every 5 seconds
