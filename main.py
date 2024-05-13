import requests
from datetime import datetime
import smtplib
import time

# Your email credentials
MY_EMAIL = "my_email@gmail.com"
MY_PASSWORD = "qwerty@1234"

# Your latitude and longitude
MY_LAT = 12.976750
MY_LONG = 77.575279

# Function to check if the ISS is overhead
def is_iss_overhead():
    # Get ISS position data from API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise exception if request fails
    data = response.json()

    # Extract ISS latitude and longitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS is within 5 degrees of user's position
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

# Function to check if it's night time
def is_night():
    # Parameters for sunrise-sunset API request
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # Get sunrise and sunset times from API
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raise exception if request fails
    data = response.json()

    # Extract sunrise and sunset hours
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get current hour
    time_now = datetime.now().hour

    # Check if it's night time
    if time_now >= sunset or time_now <= sunrise:
        return True

# Continuously check for ISS overhead at night
while True:
    time.sleep(60)  # Wait for 60 seconds before next check
    if is_iss_overhead() and is_night():  # Check if ISS is overhead and it's night time
        connection = smtplib.SMTP("smtp.gmail.com")  # Establish SMTP connection
        connection.starttls()  # Initiate TLS encryption
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login to email account
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Look Up\n\nThe ISS is above you in the sky."  # Email message
        )
