import json
import uuid
from sqlalchemy.sql import select
from database_connection import engine, events

def events_post(request):

    request_json_data = request.get_json()

    stmt = events.insert().values( \
        event_id=str(uuid.uuid1()),\
        name=request_json_data["name"],\
        date=request_json_data["date"],\
        status=request_json_data["status"] )

    conn = engine.connect()
    conn.execute(stmt)

    return "", 200

def events_get():

    events_json = []
    conn = engine.connect()

    query = (select(
        events.c.event_id,
        events.c.name,
        events.c.date,
        events.c.status))

    result = conn.execute(query)

    for row in result:
        events_json.append({
            "event_id": row["event_id"],
            "name": row["name"],
            "date": row["date"],
            "status": row["status"]})

    return json.dumps(events_json)

def events_put(request):

    event_id = request.args.get("id")
    event_json = request.get_json()

    stmt = events.update().where(
        events.c.event_id == event_id).values(
            status=event_json["status"] )

    conn = engine.connect()
    conn.execute(stmt)

    return "", 200

def events_delete(request):
    print(type(request.args.get("id")))
    stmt = (events.delete()
        .where(events.c.event_id == request.args.get("id"))
        )

    conn = engine.connect()
    conn.execute(stmt)

    return "", 200
