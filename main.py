import asyncio
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)


@app.post('/items')
async def create_item(item: dict):
    session = Session()
    item_dict = {key: value for key, value in item.items()}
    item_model = Item(**item_dict)
    session.add(item_model)
    session.commit()
    return item_model


class Item(object):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(255))