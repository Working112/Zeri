from flask import Flask, request, jsonify, send_file
import requests

app = Flask(__name__, static_folder="", template_folder="")  # Root directory

# Route to serve the HTML file
@app.route("/")
def home():
    return send_file("index.html")  # Serve index.html directly

# Route to fetch weather data
@app.route("/weather", methods=["GET"])
def get_weather():
    try:
        # Get latitude and longitude from query parameters
        latitude = request.args.get("latitude")
        longitude = request.args.get("longitude")

        if not latitude or not longitude:
            return jsonify({"error": "Latitude and longitude are required!"}), 400

        # Open-Meteo API URL (fetching multiple data points)
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&hourly=temperature_2m,precipitation_probability,wind_speed_10m,"
            f"humidity_2m,cloudcover_mid,pressure_msl,visibility"
        )

        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), response.status_code

        # Extract and return weather data
        weather_data = response.json()
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
