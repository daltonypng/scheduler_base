from flask import Flask, request
from events import events_post, events_put, events_delete, events_get
from database_connection import create_database_tables

create_database_tables()

app = Flask(__name__)

@app.route("/events", methods=["GET", "POST", "PUT", "DELETE"])

def endpoint_events():

    match request.method:

        case "POST":
            response = events_post(request)

        case "PUT":
            response = events_put(request)

        case "DELETE":
            response = events_delete(request)

        case _:
            response = events_get()

    return response
