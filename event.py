import uuid

class Event:

    def __init__(self):
        self.event_id = ""
        self.name = ""
        self.date = ""
        self.status = ""

    #*****************************************************************************#
    def post(self, request_json_data):

        self.event_id = str(uuid.uuid1())
        self.name = request_json_data["name"]
        self.date = request_json_data["date"]
        self.status = request_json_data["status"]

        return self
    #*****************************************************************************#
    def get_id(self):
        return self.event_id
    #*****************************************************************************#
    def get(self):
        return {"name": self.name, \
                "date": self.date, \
                "status": self.status}
    #*****************************************************************************#
    def put(self, request_json_data):

        self.name = request_json_data["name"]
        self.date = request_json_data["date"]
        self.status = request_json_data["status"]
