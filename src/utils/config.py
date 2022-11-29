from conexion.mongo_queries import MongoQueries
import pandas as pd

MENU_SPLIT = """
========================================
"""
MENU_INICIAL = """
============= Menu Inicial =============
[1] - Realizar Login
[0] - Sair
========================================
"""

MENU_LOGIN = """
============ Realizar Login ============
Para retornar, digite 0
"""

MENU_ADMIN = """
============= Acesso de Adm ============
[1] - Ver Relatórios
[2] - Alterar Registros
[3] - Criar Registros
[4] - Deletar Registros
[0] - Sair
========================================
"""

MENU_ADMIN_REPORTS = """
========== Ralatórios de Adm ===========
[1] - Ver Relatórios de Album
[2] - Ver Relatórios de Cartas
[3] - Ver Relatórios de Usuários
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_ALBUM_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Titulo
[2] - Alterar Descrição
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_USER_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Username
[2] - Alterar Senha
[3] - Alterar Tipo de Acesso
[0] - Sair
========================================
"""

MENU_ADMIN_CHANGE_RECORDS_CARD_OPTIONS= """
========= Alterações Permitidas ========
[1] - Alterar Imagem
[2] - Alterar Nome
[0] - Sair
========================================
"""

MENU_ADMIN_CREATE_RECORDS_CONTINUE= """
==== Deseja Inserir Mais Registros? ====
[1] - Sim
[2] - Não
========================================
"""

MENU_ADMIN_DELETE_RECORDS_CONTINUE= """
==== Deseja Deletar Mais Registros? ====
[1] - Sim
[2] - Não
========================================
"""

MENU_ADMIN_UPDATE_RECORDS_CONTINUE= """
==== Deseja Alterar Mais Registros? ====
[1] - Sim
[2] - Não
========================================
"""

MENU_ADMIN_COMFIRM_RECORDS= """
====== Você Confirma a Operação? =======
[1] - Confirmar
[2] - Cancelar
========================================
"""

MENU_ADMIN_CHANGE_RECORDS = """
=========== Alterar Registros ==========
"""

MENU_ADMIN_ALBUNS_AVAIBLES = """
========== Albúns Disponíveis ==========
"""

MENU_ADMIN_USERS_AVAIBLES = """
========= Usuários Disponíveis =========
"""

MENU_ADMIN_CARDS_AVAIBLES = """
========== Cartas Disponíveis ==========
"""

MENU_ADMIN_USER_CARD_AVAIBLES = """
========= User Card Disponíveis =========
"""

MENU_ADMIN_CREATE_RECORDS = """
============ Criar Registros ============
"""

MENU_ADMIN_DELETE_RECORDS = """
=========== Deletar Registros ===========
"""

MENU_CONFIRM_CASCATE = """
=========== Confirmar Cascade ===========
Existem outros registros que dependem desse
Quer remover o registro e seus dependentes?
[1] - Sim
[2] - Não
=========================================
"""
mongo = MongoQueries()

def login(username, password):
    mongo.connect()
    username_attempt = pd.DataFrame(list(mongo.db["user"].find({"name":f"{username}", "password":f"{password}"})))
    if not username_attempt.empty:
        return int(username_attempt.iloc[0]["access_type"])
    else:
        return 2

def search_tables(): #Método de pesquisar coleções, alterar tabelas para conexão -- ARRUMAR
    oracle = OracleQueries()
    oracle.connect()
    return(oracle.sqlToDataFrame("select table_name from user_tables"))

# Consulta de contagem de registros por tabela
def query_count(collection_name):
   from conexion.mongo_queries import MongoQueries
   import pandas as pd

   mongo = MongoQueries()
   mongo.connect()

   my_collection = mongo.db[collection_name]
   total_documentos = my_collection.count_documents({})
   mongo.close()
   df = pd.DataFrame({f"total_{collection_name}": [total_documentos]})
   return df

def clear_console(wait_time:int=3):
    '''
       Esse método limpa a tela após alguns segundos
       wait_time: argumento de entrada que indica o tempo de espera
    '''
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")