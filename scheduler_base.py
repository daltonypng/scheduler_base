from flask import Flask, request
from events import Events

app = Flask(__name__)

events = Events()

@app.route("/events", methods=["GET", "POST", "PUT", "DELETE"])

def endpoint_events():

    if request.method == "POST":
        return events.post(request)

    if request.method == "PUT":
        return events.put(request)

    if request.method == "DELETE":
        return events.delete(request)

    return events.get()
