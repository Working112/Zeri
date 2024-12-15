from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/square", methods=["POST"])
def calculate_square():
    data = request.json  # Get JSON data from the frontend
    number = data.get("number")
    
    if number is None:
        return jsonify({"error": "No number provided"}), 400

    try:
        number = float(number)  # Convert input to a float
        result = number ** 2
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
