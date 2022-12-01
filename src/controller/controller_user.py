from typing import Optional
from conexion.mongo_queries import MongoQueries
from model.user import User

class UserController:

    def __init__(self):
        pass
        self.mongo = MongoQueries()

    def inserirUser(self, name: str, password: str, access_type: int) -> User:
        self.mongo.connect()
        self.mongo.db["user"].insert_one({'name': name, 'password': password, 'access_type': access_type})
        
    def removerUser(self, name):
        self.mongo.connect()
        self.mongo.db["user"].delete_one({"name": f"{name}"})

    def atualizarUser(self, name: str, new_name: Optional[str], new_password: Optional[str], new_access_type: Optional[int], change: int):
        self.mongo.connect()
        if change == 1:
            self.mongo.db["user"].update_one({"name": f"{name}"}, {"$set": {"name": new_name}})
        if change == 2:
            self.mongo.db["user"].update_one({"name": f"{name}"}, {"$set": {"password": new_password}})
        if change == 3:
            self.mongo.db["user"].update_one({"name": f"{name}"}, {"$set": {"access_type": new_access_type}})
