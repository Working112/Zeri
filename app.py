from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__, static_folder="static", template_folder="")
CORS(app)  # Enable CORS for all routes

# Route to serve the HTML file
@app.route("/")
def home():
    return send_file("index.html")  # Serve index.html

# Route to serve static files (images)
@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)

# Route to fetch weather data
@app.route("/weather", methods=["GET"])
def get_weather():
    try:
        # Get latitude and longitude from query parameters
        latitude = request.args.get("latitude")
        longitude = request.args.get("longitude")

        if not latitude or not longitude:
            return jsonify({"error": "Latitude and longitude are required!"}), 400

        # Open-Meteo API URL (simplified with fewer variables)
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={latitude}&longitude={longitude}"
            f"&hourly=temperature_2m,precipitation_probability,wind_speed_10m"
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
