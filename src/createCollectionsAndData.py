import logging

from pandas import DataFrame
from conexion.mongo_queries import MongoQueries
import json
import math
from cards import cardsDic

LIST_OF_COLLECTIONS = ["album", "user", "card"]
logger = logging.getLogger(name="Example_CRUD_MongoDB")
logger.setLevel(level=logging.WARNING)
mongo = MongoQueries()

def createCollections(drop_if_exists:bool=False):
    """
        Lista as coleções existentes, verificar se as coleções padrão estão entre as coleções existentes.
        Caso exista e o parâmetro de exclusão esteja configurado como True, irá apagar a coleção e criar novamente.
        Caso não exista, cria a coleção.
        
        Parameter:
                  - drop_if_exists: True  -> apaga a tabela existente e recria
                                    False -> não faz nada
    """
    mongo.connect()
    existing_collections = mongo.db.list_collection_names()
    for collection in LIST_OF_COLLECTIONS:
        if collection in existing_collections:
            if drop_if_exists:
                mongo.db.drop_collection(collection)
                logger.warning(f"{collection} droped!")
                mongo.db.create_collection(collection)
                logger.warning(f"{collection} created!")
        else:
            mongo.db.create_collection(collection)
            logger.warning(f"{collection} created!")
    with open("albums.json", "r") as f:
            albums = json.load(f)
    mongo.db["album"].insert_many(albums)
    dictCards = cardsDic()
    for x in range(len(dictCards)):
        mongo.db["album"].update_one({ "title": str(dictCards[x][0]['album']) }, {
                 "$set": {
                    "card_count": len(dictCards[x]),
                    "page_count": math.floor(len(dictCards[x])/10)
                 }})
        mongo.db.get_collection("card").insert_many(dictCards[x])
    mongo.close()

def insert_many(data:json, collection:str):
    mongo.connect()
    mongo.db[collection].insert_many(data)
    mongo.close()

if __name__ == "__main__":
    logging.warning("Starting")
    createCollections(drop_if_exists=True)
    with open("users.json", "r") as f:
            users = json.load(f)
    insert_many(users, "user")
    logging.warning("End")
