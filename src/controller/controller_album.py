from typing import Optional
from conexion.mongo_queries import MongoQueries
from model.album import Album

class AlbumController:

    def __init__(self):
        pass
        self.mongo = MongoQueries()

    def inserirAlbum(self, title: str, card_count: int, page_number: int, description: str) -> Album:
        self.mongo.connect()
        self.mongo.db["album"].insert_one({'title': title, 'card_count': card_count, 'page_count': page_number, 'description': description})
        
    def removerAlbum(self, title: str):
        self.mongo.connect()
        self.mongo.db["album"].delete_one({"title": f"{title}"})

    def atualizarAlbum(self, title: str, new_title: Optional[str], new_description: Optional[str], change: int):
        self.mongo.connect()
        if change == 1:
            self.mongo.db["album"].update_one({"title": f"{title}"}, {"$set": {"title": new_title}})
        if change == 2:
            self.mongo.db["album"].update_one({"title": f"{title}"}, {"$set": {"description": new_description}})
