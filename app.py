from flask import Flask, send_file, request, jsonify

app = Flask(__name__)

# Route to serve the index.html file
@app.route("/")
def home():
    try:
        return send_file("index.html")  # Ensure index.html is in the root directory
    except Exception as e:
        return f"Error: {e}", 500

# Simple API route to calculate the square of a number
@app.route("/square", methods=["GET"])
def calculate_square():
    try:
        number = request.args.get("number")
        if not number:
            raise ValueError("No number provided")

        number = float(number)  # Convert input to a number
        result = number ** 2
        return jsonify({"result": result})  # Return the square as JSON
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

# Default Flask run configuration
if __name__ == "__main__":
    app.run(debug=True)
