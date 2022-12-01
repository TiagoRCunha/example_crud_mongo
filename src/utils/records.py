from pandas import DataFrame
from conexion.mongo_queries import MongoQueries

class Records: 

    def __init__(self):
        self.created_by = "Henrique Klayton, Tiago Rodrigues e Victor Binda"
        self.mongo = MongoQueries()

    def select_admin_album_view(self) -> DataFrame:
        self.mongo.connect()
        return DataFrame(self.mongo.db["album"].find())
    
    def select_admin_card_view(self) -> DataFrame:
        self.mongo.connect()
        return self.oracle.sqlToDataFrame("select * from admin_card_view") #alterar

    def select_admin_users_view(self) -> DataFrame:
        self.mongo.connect()
        return self.oracle.sqlToDataFrame("select * from admin_users_view") #alterar
    
    def total_albuns(self) -> int:
        self.mongo.connect()
        return int(self.mongo.db['album'].count_documents({}))

    def list_albuns(self) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['album'].find()))

    def show_album(self, title) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['album'].find({"title":f"{title}"})))

    def total_users(self) -> int:
        self.mongo.connect()
        return int(self.mongo.db['user'].count_documents({}))

    def list_users(self) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['user'].find()))

    def show_user(self, name) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['user'].find({"name":f"{name}"})))

    def total_cards(self) -> int:
        self.mongo.connect()
        return int(self.mongo.db['card'].count_documents({}))

    def list_cards(self) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['card'].find()))

    def list_cards_with_pagination(self, offset) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['card'].find().skip(offset).limit(5)))

    def show_card(self, card) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['card'].find({"name":f"{card}"})))

    def show_card_by_number(self, card) -> DataFrame:
        self.mongo.connect()
        return DataFrame(list(self.mongo.db['card'].find({"number": card})))


    def get_init(self) -> str:
        return f"""
    Bem vindo ao Album Digital
Desenvolvedores: {self.created_by}
   
====== Total de Registro no Banco ======
Usuários: {self.total_users()}
Albuns: {self.total_albuns()}
Cartas: {self.total_cards()}
========================================
"""
