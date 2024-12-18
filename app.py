from flask import Flask, request, jsonify, send_file
import requests

app = Flask(__name__, static_folder="", template_folder="")

@app.route("/")
def home():
    return send_file("index.html")  

@app.route("/weather", methods=["GET"])
def get_weather():
    try:
        # Get latitude and longitude
        latitude = request.args.get("latitude")
        longitude = request.args.get("longitude")

        if not latitude or not longitude:
            return jsonify({"error": "Latitude and longitude are required!"}), 400

        # Open-Meteo API URL
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), response.status_code

        # Return weather data as JSON
        weather_data = response.json()
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
