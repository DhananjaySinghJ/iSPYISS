# ISS Tracker

This Python script tracks the International Space Station (ISS) and sends an email notification when the ISS is overhead during the night.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3
- Required Python packages: `requests`, `smtplib`

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/iss-tracker.git

2. Navigate to the project directory: cd iss-tracker

3.Update the following variables in the iss_tracker.py file:

MY_EMAIL: Your Gmail email address.
MY_PASSWORD: Your Gmail password (You might need to generate an App Password).
MY_LAT: Your latitude.
MY_LONG: Your longitude.

4. Run the script:python main.py

How it Works
The script makes use of two APIs:

Open Notify API: To get the current location of the ISS.
Sunrise-Sunset API: To get the sunrise and sunset times at the specified location.
It continuously checks whether the ISS is overhead and whether it is night time at the specified location.

If the conditions are met, it sends an email notification.

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

License
MIT

