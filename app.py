from flask import Flask, jsonify

app = Flask(__name__)

kill_switch = {"kill": False}

@app.route("/killswitch", methods=["GET"])
def get_kill_switch():
    return jsonify(kill_switch)

@app.route("/killswitch/on", methods=["POST"])
def turn_on():
    kill_switch["kill"] = True
    return jsonify({"message": "Kill switch ON"})

@app.route("/killswitch/off", methods=["POST"])
def turn_off():
    kill_switch["kill"] = False
    return jsonify({"message": "Kill switch OFF"})

@app.route("/", methods=["GET"])
def home():
    return "Kill switch server is running!"

if __name__ == "__main__":
    app.run()
