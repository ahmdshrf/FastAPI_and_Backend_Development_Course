from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session


engine = create_engine(
    url="sqlite:///sqlite.db",
    echo= True,
    connect_args= {"check_same_thread":False},
)
from .models import Shipment
def create_db_tables():
    SQLModel.metadata.create_all(bind=engine)


session = Session(bind= engine)
session.get(
    Shipment,
    12078
)
session.add(
    Shipment(id=12071)
)

session.commit()