from typing import Optional
from controller.controller_rarity import RarityController
from controller.controller_background import BackgroundController
from controller.controller_tag import TagController
from controller.controller_album import AlbumController
from controller.controller_border import BorderController
from controller.controller_card import CardController
import utils.config as config
from utils.records import Records

def select_album_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
        albuns_list = Records().list_albuns()
        for x in range(albuns_list.shape[0]):
            print(f"{x + 1} - " + albuns_list.iloc[x]["title"])
        print(config.MENU_SPLIT)
        id = input("Digite o número do album que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_album(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_album(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_album(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None
  
def update_album(id):
    show_album = Records().show_album(id)

    print("As informações do album disponíveis para alteração são:\n")
    for x in range(show_album.shape[0]):
        print(show_album.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_ALBUM_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_title = input("Insira o novo titulo para o album\n")
            if new_title == "0":
                config.clear_console(1)
                return 0
            AlbumController().update(id, new_title, None, 1)
            break
        elif selection == 2:
            new_description = input("Insira a nova descrição do album\n")
            if new_description == "0":
                config.clear_console(1)
                return 0
            AlbumController().update(id, None, new_description, 2)
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_user_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_USERS_AVAIBLES)
        users_list = Records().list_users()
        for x in range(users_list.shape[0]):
            print(f"{x + 1} - " + users_list.iloc[x]["username"])
        print(config.MENU_SPLIT)
        id = input("Digite o número do usuário que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_user(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_user(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_user(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None


#TODO
def update_user(id):
    show_user = Records().show_user(id)

    print("As informações do usuário disponíveis para alteração são:\n")
    for x in range(show_user.shape[0]):
        print(show_user.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_USER_OPTIONS)
    selection = int(input("Digite sua opção, ou aperte 'Enter' para sair\n"))
    loop = True
    while loop:
        if selection == 1:
            new_username = input("Insira o novo username para o usuário\n")
            if new_username == "":
                config.clear_console(1)
                return 0
            #UPDATE USERNAME USER
            break
        elif selection == 2:
            new_password = input("Insira a nova senha do usuário\n")
            if new_password == "":
                config.clear_console(1)
                return 0
            #UPDATE SENHA USER
            break
        elif selection == 3:
            new_access_type = input("Insira o novo tipo de acesso do usuário [0 = Normal, 1 = Admin]\n")
            while new_access_type != "0" and new_access_type != "1" and new_access_type != "":
                new_access_type = input("Tipo de acesso inválido, insira novamente [0 = normal, 1 = admin]\n")
            if new_access_type == "":
                config.clear_console(1)
                return 0
            #UPDATE TIPO DE ACESSO USER
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_card_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_CARDS_AVAIBLES)
        cards_list = Records().list_cards()
        for x in range(cards_list.shape[0]):
            print(f"{x + 1} - " + cards_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da carta que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_card(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_card(id)
        if not id_verification.empty:
            config.clear_console(1)
            if update_card(id) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

#TODO
def update_card(id):
    show_card = Records().show_card(id)

    print("As informações da carta disponíveis para alteração são:\n")
    for x in range(show_card.shape[0]):
        print(show_card.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_CARD_OPTIONS)
    selection = int(input("Digite sua opção\n"))
    loop = True
    while loop:
        if selection == 1:
            new_image = input("Insira a nova imagem da carta\n")
            if new_image == "0":
                config.clear_console(1)
                return 0
            CardController().update(id, new_image, None, 1)
            break
        elif selection == 2:
            new_name = input("Insira o novo nome da carta\n")
            if new_name == "0":
                config.clear_console(1)
                return 0
            CardController().update(id, None, new_name, 1)
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def menu_continue():
    config.clear_console(1)
    print(config.MENU_ADMIN_UPDATE_RECORDS_CONTINUE)
    selection = str(input("Insira sua opção\n"))
    if selection == "2":
        config.clear_console(1)
        return 2
    config.clear_console(1)
