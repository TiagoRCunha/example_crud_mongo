from typing import Optional
from conexion.mongo_queries import MongoQueries
from model.card import Card

class CardController:

    def __init__(self):
        pass
        self.mongo = MongoQueries()

    def inserirCarta(self, number:int=None, image:str=None, name:str=None, background:str=None, border:str=None, rarity:int=None, album:str=None) -> Card:
        self.mongo.connect()
        self.mongo.db["card"].insert_one({'number': number, 'image': image, 'name': name, 'background': background, 'border': border, 'rarity': rarity, 'album': album})
        
    def removerCarta(self, card):
        self.mongo.connect()
        self.mongo.db["card"].delete_one({"name": f"{card}"})

    def atualizarCarta(self, name: str, new_image: Optional[str], new_name: Optional[str], change: int):
        self.mongo.connect()
        if change == 1:
            self.mongo.db["card"].update_one({"name": f"{name}"}, {"$set": {"image": new_image}})
        if change == 2:
            self.mongo.db["card"].update_one({"name": f"{name}"}, {"$set": {"name": new_name}})
