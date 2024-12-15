from flask import Flask, send_file

app = Flask(__name__)

# Route to serve the index.html file
@app.route("/")
def home():
    try:
        return send_file("index.html")  # Make sure index.html is in the root folder
    except Exception as e:
        return f"Error: {e}", 500

if __name__ == "__main__":
    app.run(debug=True)
