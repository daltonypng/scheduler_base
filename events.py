import json
from event import Event

class Events:

    def __init__(self):
        self.list = {}

    #*****************************************************************************#
    def post(self, request):

        event = Event()
        event.post(request.get_json())
        self.list[event.get_id()] = event
        return event.get_id(), 200
    #*****************************************************************************#
    def get(self):

        events_json = {}

        for event_id in self.list:
            events_json[event_id] = self.list[event_id].get()

        return json.dumps(events_json)
    #*****************************************************************************#
    def put(self, request):

        event_id = request.args.get("id")
        event_json = request.get_json()

        if event_id in self.list:
            self.list[event_id].put(event_json)

            return "", 200

        return "Evento não cadastrado para essa ID", 500
    #*****************************************************************************#
    def delete(self, request):

        event_id = request.args.get("id")

        if event_id in self.list:
            del self.list[event_id]

            return "", 200

        return "Evento não cadastrado para essa ID", 500
