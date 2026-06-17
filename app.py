""" 
The goal of this project is to build a scalable RESTful API around 
openSenseMap but customized to help beekeepers with their chores.  
"""

from datetime import datetime, timezone
from fastapi import FastAPI
import requests
from prometheus_fastapi_instrumentator import Instrumentator


VERSION = "v0.0.1"
SENSEBOXID = "5f52892137e925001bcca76e"

app = FastAPI()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

@app.get("/version")
async def print_app_version():
    """ Return App Version """

    return f"version: {VERSION}"


@app.get("/temperature")
async def get_temperature():
    """ 
        Fetch and return the average temp from Sensebox sensors for
        the last 1 hour
    """

    url = f"https://api.opensensemap.org/boxes/{SENSEBOXID}"

    try:
        response = requests.get(url, timeout=10).json()
        sensors = response.get("sensors", [])
        status = ""
        model_response = {}

        valid_temperatures = []
        current_time = datetime.now(timezone.utc)

        for sensor in sensors:
            # Check if the sensor measures temperature
            if "temperatur" in sensor.get("title", "").lower() or \
                "temperature" in sensor.get("phenomenon", "").lower():
                last_meas = sensor.get("lastMeasurement")

                if last_meas:
                    # Parse timestamp and check data age
                    created_at = datetime.fromisoformat(last_meas["createdAt"]\
                                                        .replace("Z", "+00:00"))
                    age_minutes = (current_time - created_at).total_seconds() / 60

                    if age_minutes <= 60:
                        valid_temperatures.append(float(last_meas["value"]))
                        print(f"Sensor '{sensor['title']}': {last_meas['value']}°C \
                              (Age: {age_minutes:.1f} mins)")
                    else:
                        print(f"⚠️ Skipped '{sensor['title']}': Stale data \
                              ({age_minutes:.1f} mins old)")

        if valid_temperatures:
            avg_temp = sum(valid_temperatures) / len(valid_temperatures)
            model_response[avg_temp] = avg_temp

            if avg_temp < 10:
                model_response[status] = "Too Cold"
            elif 11 < avg_temp < 36:
                model_response[status] = "Good"
            else:
                model_response[status] =  "Too Hot"


            return {f"Average Temperature: {model_response[avg_temp]:.2f}°C",
                    f"Status: {model_response.get(status)}"}

        return "Error: No temperature sensors have reported data within the last hour."

    except (requests.RequestException, ValueError) as e:
        print(f"Network or data error: {e}")
