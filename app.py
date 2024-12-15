from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/square", methods=["GET"])
def calculate_square():
    try:
        number = float(request.args.get("number"))
        result = number ** 2
        return jsonify({"result": result})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
