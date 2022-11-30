from controller.controller_album import AlbumController
from controller.controller_card import CardController
from controller.controller_user import UserController
import utils.config as config
from utils.records import Records


def remove_album():
    loop = True
    while loop:
        print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
        albuns_list = Records().list_albuns()
        for x in range(albuns_list.shape[0]):
            print(albuns_list.iloc[x]["title"])
        print(config.MENU_SPLIT)
        album = input("Digite o nome do album que deseja remover ou 0 para sair\n")
        album_verification = Records().show_album(album)
        while album_verification.empty:
            album = input("Album inválido, insira o nome novamente ou 0 para sair\n")
            if album == "0":
                config.clear_console(1)
                return None
            album_verification = Records().show_album(album)
        if menu_confirm() == 1:
                AlbumController.removerAlbum(album)
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def remove_user():
    loop = True
    while loop:
        print(config.MENU_ADMIN_USERS_AVAIBLES)
        users_list = Records().list_users()
        for x in range(users_list.shape[0]):
            print(users_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        name = input("Digite o nome do usuário que deseja remover ou 0 para sair\n")
        user_verification = Records().show_user(name)
        while user_verification.empty:
            name = input("Usuário inválido, insira o nome do usuário novamente ou 0 para sair\n")
            if name == "0":
                config.clear_console(1)
                return None
            user_verification = Records().show_user(name)
        if menu_confirm() == 1:
                UserController.removerUser(name)
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def remove_card():
    loop = True
    while loop:
        print(config.MENU_ADMIN_CARDS_AVAIBLES)
        cards_list = Records().list_cards()
        for x in range(cards_list.shape[0]):
            print(cards_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        card = input("Digite o nome da carta que deseja alterar ou 0 para sair\n")
        card_verification = Records().show_card(card)
        while card_verification.empty:
            card = input("Carta inválido, insira o nome da carta novamente ou 0 para sair\n")
            if card == "0":
                config.clear_console(1)
                return None
            card_verification = Records().show_card(card)
        if menu_confirm() == 1:
                CardController.removerCarta(card)
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def menu_continue():
    config.clear_console(1)
    print(config.MENU_ADMIN_DELETE_RECORDS_CONTINUE)
    selection = str(input("Insira sua opção\n"))
    if selection == "2":
        config.clear_console(1)
        return 2
    config.clear_console(1)

def menu_confirm():
    config.clear_console(1)
    print(config.MENU_ADMIN_COMFIRM_RECORDS)
    selection = str(input("Insira sua opção\n"))
    if selection == "1":
        config.clear_console(1)
        return 1
    config.clear_console(1)