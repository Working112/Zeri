from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Serve the HTML file
@app.route("/")
def home():
    return render_template("index.html")

# Fetch weather data from Open-Meteo API
@app.route("/weather", methods=["GET"])
def get_weather():
    try:
        latitude = request.args.get("latitude")
        longitude = request.args.get("longitude")

        if not latitude or not longitude:
            return jsonify({"error": "Latitude and longitude are required!"}), 400

        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"
        response = requests.get(url)

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch weather data"}), response.status_code

        weather_data = response.json()
        return jsonify(weather_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
