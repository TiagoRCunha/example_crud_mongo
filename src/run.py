import utils.config as config
from utils.records import Records
from utils import create_records, remove_records, update_records

#TODO
#Verificar uso de ILOC em todo o projeto
#Alterar todos os pontos comentados nesse arquivo
#Ajeitar records.py em utils
#Ajeitar métodos de login e pesquisar tabela(coleções) em config.py em utils
#Ajeitar create_records.py em utils, verificar necessidade de controllers
#Ajeitar remove_records.py em utils
#Ajeitar update_records.py em utils

def run():
        print(Records().get_init()) # Mostra quantidade de objetos no banco -- ARRUMAR

        loop = True

        while loop:
                print(config.MENU_INICIAL)
                selection = int(input("Selecione a opção\n"))
                config.clear_console(1)
                if selection == 1:
                        config.clear_console(1)
                        login()

                elif selection == 0:
                        print("Obrigado e volte sempre!")
                        config.clear_console(1)
                        loop = False
                else:
                        selection = int(input("Opção inválida, insira novamente"))

def login():
        loop = True
        while loop:
                print(config.MENU_LOGIN)
                username = input("Insira seu username: ")
                if username == "0":
                        loop = False
                        break
                password = input("Insira sua senha: ")
                if password == "0":
                        loop = False
                        break
                access = config.login(username, password)
                if access == 0:
                        print("Login de usuário realizado com sucesso\nMenu de usuário não existente, retornando")
                        config.clear_console(1)
                        break
                elif access == 1:
                        print("Login de administrador realizado com sucesso")
                        config.clear_console(1)
                        admin_access()
                else:
                        config.clear_console(1)
                        print("Usuário ou senha incorretos, por favor tente novamente")

def admin_access():
        loop = True
        while loop:
                print(config.MENU_ADMIN)
                selection = int(input("Selecione a opção\n"))
                config.clear_console(1)
                if selection == 1:
                        admin_access_reports()
                elif selection == 2:
                        admin_access_change_records()
                elif selection == 3:
                        admin_access_create_records()
                elif selection == 4:
                        admin_access_delete_records()
                elif selection == 0:
                        loop = False
                        break

def admin_access_reports():
        loop = True
        while loop:
                print(config.MENU_ADMIN_REPORTS)
                selection = int(input("Selecione a opção\n"))
                config.clear_console(1)
                if selection == 1:
                        print(Records().select_admin_album_view()) #Ver report de album -- ARRUMAR
                        break
                elif selection == 2:
                        print(Records().select_admin_card_view()) #Ver report de cartas -- ARRUMAR
                        break
                elif selection == 3:
                        print(Records().select_admin_users_view()) #Ver report de usuarios -- ARRUMAR
                        break
                elif selection == 0:
                        loop = False
                        break

def admin_access_change_records():
        loop = True
        while loop:
                print(config.MENU_ADMIN_CHANGE_RECORDS)
                print("As tabelas disponiveis para modificação são:\n")
                table_list = config.search_tables() #Listar as coleções existentes -- ARRUMAR
                aux_list = []
                for x in range(table_list.shape[0]): #Ajeitar forma de escolher objeto -- ARRUMAR
                        aux_list.append({ "id": (x + 1), "name": table_list.iloc[x]["table_name"] })
                        print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
                print(config.MENU_SPLIT)
                selection = int(input("Digite o nome da tabela que deseja modificar, insira 0 para sair\n"))
                config.clear_console(1)
                aux_name = None
                for x in range(len(aux_list)):
                        if aux_list[x]["id"] == selection:
                                aux_name = aux_list[x]["name"]
                if aux_name == "album":
                        update_records.select_album_update() #Atualizar album -- ARRUMAR
                elif aux_name == "user":
                        update_records.select_user_update() #Atualizar usuario -- ARRUMAR
                elif aux_name == "card":
                        update_records.select_card_update() #Atualizar carta -- ARRUMAR
                elif selection == 0:
                        loop = False
                        config.clear_console(1)

def admin_access_create_records():
        loop = True
        while loop:
                print(config.MENU_ADMIN_CREATE_RECORDS)
                print("As tabelas disponiveis para inserção de valores são:\n")
                table_list = config.search_tables()
                aux_list = []
                for x in range(len(table_list)):
                        aux_list.append({ "id": (x + 1), "name": table_list[x]})
                        print(f"{x + 1} - " + table_list[x])
                print(config.MENU_SPLIT)
                selection = int(input("Digite o nome da tabela que deseja inserir um valor, insira 0 para sair\n"))
                config.clear_console(1)
                aux_name = None
                for x in range(len(aux_list)):
                        if aux_list[x]["id"] == selection:
                                aux_name = aux_list[x]["name"]
                if aux_name == "album":
                        create_records.create_album() #Criar album -- ARRUMAR
                elif aux_name == "user":
                        create_records.create_user() #Criar user -- ARRUMAR
                elif aux_name == "card":
                        create_records.create_card() #Criar carta -- ARRUMAR
                if selection == 0:
                        loop = False
                        config.clear_console(1)
                        
def admin_access_delete_records():
        loop = True
        while loop:
                print(config.MENU_ADMIN_DELETE_RECORDS)
                print("As tabelas disponiveis para remoção de valores são:\n")
                table_list = config.search_tables() #Listar as coleções existentes -- ARRUMAR
                aux_list = []
                for x in range(table_list.shape[0]): #Ajeitar forma de escolher objeto -- ARRUMAR
                        print(f"{x + 1} - " + table_list.iloc[x]["table_name"])
                print(config.MENU_SPLIT)
                selection = int(input("Digite o nome da tabela que deseja remover um valor, insira 0 para sair\n"))
                config.clear_console(1)
                aux_name = None
                for x in range(len(aux_list)):
                        if aux_list[x]["id"] == selection:
                                aux_name = aux_list[x]["name"]
                if aux_name == "album":
                        create_records.create_album() #Criar album -- ARRUMAR
                elif aux_name == "user":
                        create_records.create_user() #Criar user -- ARRUMAR
                elif aux_name == "card":
                        create_records.create_card() #Criar carta -- ARRUMAR
                if selection == 0:
                        loop = False
                        config.clear_console(1)
                config.clear_console(1)
        
run()
