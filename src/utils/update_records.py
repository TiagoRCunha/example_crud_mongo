from pandas import DataFrame
from controller.controller_album import AlbumController
from controller.controller_user import UserController
from controller.controller_card import CardController
import utils.config as config
from utils.records import Records

def select_album_update():
    loop = True
    while loop:
        print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
        albuns_list = Records().list_albuns()
        for x in range(albuns_list.shape[0]):
            print(albuns_list.iloc[x]["title"])
        print(config.MENU_SPLIT)
        title = input("Digite o nome do album que deseja alterar ou 0 para sair\n")
        if title == "0":
            config.clear_console(1)
            return None
        title_verification = Records().show_album(title)
        while title_verification.empty:
            title = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if title == "0":
                config.clear_console(1)
                return None
            title_verification = Records().show_album(id)
        if not title_verification.empty:
            config.clear_console(1)
            if update_album(title) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None
  
def update_album(title):
    show_album = Records().show_album(title)

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
            AlbumController().atualizarAlbum(title, new_title, None, 1)
            break
        elif selection == 2:
            new_description = input("Insira a nova descrição do album\n")
            if new_description == "0":
                config.clear_console(1)
                return 0
            AlbumController().atualizarAlbum(id, None, new_description, 2)
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
            print(users_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        name = input("Digite o nome do usuário que deseja alterar ou 0 para sair\n")
        if name == "0":
            config.clear_console(1)
            return None
        name_verification = Records().show_user(name)
        while name_verification.empty:
            name = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if name == "0":
                config.clear_console(1)
                return None
            name_verification = Records().show_user(name)
        if not name_verification.empty:
            config.clear_console(1)
            if update_user(name) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

def update_user(name):
    show_user = Records().show_user(id)

    print("As informações do usuário disponíveis para alteração são:\n")
    for x in range(show_user.shape[0]):
        print(show_user.iloc[0])
    print("\n", config.MENU_ADMIN_CHANGE_RECORDS_USER_OPTIONS)
    selection = int(input("Digite sua opção, ou aperte 'Enter' para sair\n"))
    loop = True
    while loop:
        if selection == 1:
            new_name = input("Insira o novo username para o usuário\n")
            if new_name == "":
                config.clear_console(1)
                return 0
            UserController().atualizarUser(name, new_name, None, None, 1)
            break
        elif selection == 2:
            new_password = input("Insira a nova senha do usuário\n")
            if new_password == "":
                config.clear_console(1)
                return 0
            UserController().atualizarUser(name, None, new_password, None, 2)
            break
        elif selection == 3:
            new_access_type = input("Insira o novo tipo de acesso do usuário [0 = Normal, 1 = Admin]\n")
            while new_access_type != "0" and new_access_type != "1" and new_access_type != "":
                new_access_type = input("Tipo de acesso inválido, insira novamente [0 = normal, 1 = admin]\n")
            if new_access_type == "":
                config.clear_console(1)
                return 0
            UserController().atualizarUser(name, None, None, new_access_type, 3)
            break
        elif selection == 0:
            config.clear_console(1)
            return 0

def select_card_update():
    loop = True
    number = " "
    offset = 0
    number_verification = DataFrame()
    while loop:
        print(config.MENU_ADMIN_CARDS_AVAIBLES)
        if number == "<":
            offset = offset - 5
        elif number == ">":
            offset = offset + 5
        elif number == ">>":
            offset = offset + 40
        cards_list = Records().list_cards_with_pagination(offset)
        for x in range(cards_list.shape[0]):
            print(str(cards_list.iloc[x]["number"]) + " " + cards_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        print("Trocar de página digite '<' para voltar, '>' para avançar, ou '>>' para avançar 40 linhas")
        number = input("Digite o numero da carta que deseja alterar ou 0 para sair \n")
        if number not in "<" and number not in ">>":
            number_verification = Records().show_card_by_number(int(number))
        if number == "0":
            config.clear_console(1)
            return None
        while number_verification.empty and not number in "<" and not number in ">>":
            number = input("\nOpção inválida, digite novamente ou 0 para sair \n")
            if number == "0":
                config.clear_console(1)
                return None
            number_verification = Records().show_card_by_number(int(number))
        if not number_verification.empty and not number in "<" and not number in ">>":
            config.clear_console(1)
            if update_card(int(number)) == 0:
                return None
            config.clear_console(1)
            if menu_continue() == 2:
                return None

def update_card(number):
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
            CardController().atualizarCarta(number, new_image, None, 1)
            break
        elif selection == 2:
            new_name = input("Insira o novo nome da carta\n")
            if new_name == "0":
                config.clear_console(1)
                return 0
            CardController().atualizarCarta(number, None, new_name, 2)
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
