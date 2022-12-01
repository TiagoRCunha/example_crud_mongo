from typing import Optional

from pandas import DataFrame
from conexion.mongo_queries import MongoQueries
from controller.controller_album import AlbumController
from model.card import Card

class CardController:

    def __init__(self):
        pass
        self.mongo = MongoQueries()

    def inserirCarta(self, number:int=None, image:str=None, name:str=None, background:str=None, border:str=None, rarity:int=None, album:str=None) -> Card:
        self.mongo.connect()
        self.mongo.db["card"].insert_one({'number': number, 'image': image, 'name': name, 'background': background, 'border': border, 'rarity': rarity, 'album': album})
        card = DataFrame(self.mongo.db["card"].find({ "number": number }))
        AlbumController().atualizarAlbumContagem(card.iloc[0]["album"], 1)
        
    def removerCarta(self, card):
        self.mongo.connect()
        card = DataFrame(self.mongo.db["card"].find({ "name": str(card) }))
        self.mongo.db["card"].delete_one({"name": f"{card}"})
        AlbumController().atualizarAlbumContagem(card.iloc[0]["album"], -1)

    def atualizarCarta(self, number: str, new_image: Optional[str], new_name: Optional[str], change: int):
        self.mongo.connect()
        if change == 1:
            self.mongo.db["card"].update_one({"number": number }, {"$set": {"image": new_image}})
        if change == 2:
            self.mongo.db["card"].update_one({"number": number }, {"$set": {"name": new_name}})