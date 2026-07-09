from flask import Flask, request, jsonify
from TDU_Nucleus_Suite import TDUNucleus

app = Flask(__name__)
nucleus = TDUNucleus()

@app.route("/route", methods=["POST"])
def route_signal():
    data = request.json
    signal = data.get("signal", "")
    mode = data.get("assistant", "")
    output = nucleus.route(signal, mode)
    return jsonify({"result": output})

if __name__ == "__main__":
    app.run(debug=True)
