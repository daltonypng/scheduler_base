from sqlalchemy import create_engine, Table, Column, String, MetaData

engine = create_engine("sqlite:///schedule.db", echo=False)

current_db_metadata = MetaData()

events = Table(
    "events",
    current_db_metadata,
    Column("event_id", String(32), primary_key=True),
    Column("name", String),
    Column("date", String(10)),
    Column("status", String),
)

def create_database_tables():
    current_db_metadata.create_all(engine)
