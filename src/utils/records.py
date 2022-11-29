from pandas import DataFrame
from conexion.oracle_queries import OracleQueries

class Records: #Alterar todas as pesquisas para mongo

    def __init__(self):
        self.created_by = "Henrique Klayton, Tiago Rodrigues e Victor Binda"
        self.oracle = OracleQueries()

    def select_admin_album_view(self) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select * from admin_album_view")
    
    def select_admin_card_view(self) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select * from admin_card_view")

    def select_admin_users_view(self) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select * from admin_users_view")
    
    def total_albuns(self) -> int:
        self.oracle.connect()
        return int(self.oracle.sqlToDataFrame("select count(*) from labdatabase.\"album\"").iloc[0])

    def list_albuns(self) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select title from labdatabase.\"album\"")

    def show_album(self, id) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame(f"select title, \"description\" from labdatabase.\"album\" where id = '{id}'")

    def total_users(self) -> int:
        self.oracle.connect()
        return int(self.oracle.sqlToDataFrame("select count(*) from labdatabase.\"user\"").iloc[0])

    def list_users(self) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select username from labdatabase.\"user\"")

    def show_user(self, id) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame(f"select username, \"password\", access_type from labdatabase.\"user\" where id = '{id}'")

    def total_cards(self) -> int:
        self.oracle.connect()
        return int(self.oracle.sqlToDataFrame("select count(*) from labdatabase.\"card\"").iloc[0])

    def list_cards(self) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame("select \"name\" from labdatabase.\"card\"")

    def show_card(self, id) -> DataFrame:
        self.oracle.connect()
        return self.oracle.sqlToDataFrame(f"select \"image\", \"name\" from labdatabase.\"card\" where id = '{id}'")

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
