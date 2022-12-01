import utils.config as config
from utils.records import Records
from controller.controller_album import AlbumController
from controller.controller_user import UserController
from controller.controller_card import CardController

def create_album():
    loop = True
    while loop:
        print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
        albuns_list = Records().list_albuns()
        for x in range(albuns_list.shape[0]):
            print(albuns_list.iloc[x]["title"])
        print(config.MENU_SPLIT)
        print("Criação de album\nDurante as opções, para sair digite '0'")
        title = input("Digite o título do album\n")
        if title == "0":
            config.clear_console(1)
            return None
        card_count = 0
        page_number = 0
        description = input("Digite a descrição do album\n")
        if description == "0":
            config.clear_console(1)
            return None
        AlbumController().inserirAlbum(title, card_count, page_number, description)
        if menu_continue() == 2:
            return None
        config.clear_console(1)


def create_user():
    loop = True
    userCtrl = UserController()
    while loop:
        print(config.MENU_ADMIN_USERS_AVAIBLES)
        users_list = Records().list_users()
        for x in range(users_list.shape[0]):
            print(users_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        print("Criação de usuário\nDurante as opções, para sair aperte 'ENTER'")
        username = input("\nDigite o username do usuário\n")
        if username == "":
            config.clear_console(1)
            return None
        password = input("Digite a senha do usuário\n")
        if password == "":
            config.clear_console(1)
            return None
        access_type = input("Digite o tipo de acesso do usuário [0 = normal, 1 = admin]\n")
        while access_type != "0" and access_type != "1" and access_type != "":
            access_type = input("Tipo de acesso inválido, insira novamente [0 = normal, 1 = admin]\n")
        if access_type == "":
            config.clear_console(1)
            return None
        userCtrl.inserirUser(username, password, access_type)
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def select_album():
    print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
    albuns_list = Records().list_albuns()
    for x in range(albuns_list.shape[0]):
        print(albuns_list.iloc[x]["title"])
    print(config.MENU_SPLIT)
    album = input("Digite o nome do album que deseja selecionar ou 0 para sair\n")
    loop = True
    while loop:
        album_verification = Records().show_album(album)
        if album == "0":
            loop = False
            config.clear_console(1)
            return 0
        elif not album_verification.empty:
            config.clear_console(1)
            return album
        while album_verification.empty:
            album = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

def create_card():
    loop = True
    while loop:
        print(config.MENU_ADMIN_CARDS_AVAIBLES)
        cards_list = Records().list_cards()
        print("Atualmente existem: " + str(cards_list.shape[0]) + " cartas")
        print("Ultima carta criada: " + str(cards_list.iloc[-1]["name"]) + " [" + str(cards_list.iloc[-1]["number"]) + "]")
        print(config.MENU_SPLIT)
        print("Criação de cartas\nDurante as opções, para sair digite '0'")
        number = input("Digite o número da carta\n")
        if number == "0":
            config.clear_console(1)
            return None
        image = input("Digite o arquivo de imagem da carta\n")
        if image == "0":
            config.clear_console(1)
            return None
        name = input("Digite o nome da carta\n")
        if name == "0":
            config.clear_console(1)
            return None
        background = input("Digite o nome do arquivo do background\n")
        if background == 0:
            config.clear_console(1)
            return None
        border = input("Digite o nome do arquivo da borda\n")
        if border == 0:
            config.clear_console(1)
            return None
        rarity = int(input("Digite o nivel de raridade da carta entre 1 e 5\n"))
        while rarity < 1 or rarity > 5:
            rarity = input("Nivel de raridade inexistente, digite um nivel entre 1 e 5, ou digite 0 para sair\n")
            config.clear_console(1)
            if rarity == 0:
                config.clear_console(1)
                return None
        if rarity == 0:
            config.clear_console(1)
            return None
        album = select_album()
        if album == 0:
            config.clear_console(1)
            return None
        CardController().inserirCarta(number, image, name, background, border, rarity, album)
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def menu_continue():
    config.clear_console(1)
    print(config.MENU_ADMIN_CREATE_RECORDS_CONTINUE)
    selection = str(input("Insira sua opção\n"))
    if selection == "2":
        config.clear_console(1)
        return 2
    config.clear_console(1)