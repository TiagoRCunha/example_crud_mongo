import utils.config as config
from utils.records import Records
from controller.controller_album import AlbumController
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
        card_count = input("Quantas cartas o album possuirá?\n")
        if card_count == "0":
            config.clear_console(1)
            return None
        page_number = input("Quantas páginas o album possuirá?\n")
        if page_number == "0":
            config.clear_console(1)
            return None
        description = input("Digite a descrição do album\n")
        if description == "0":
            config.clear_console(1)
            return None
        AlbumController().insert(title, card_count, page_number, description)
        if menu_continue() == 2:
            return None
        config.clear_console(1)


def create_user():
    loop = True
    while loop:
        print(config.MENU_ADMIN_USERS_AVAIBLES)
        users_list = Records().list_users()
        for x in range(users_list.shape[0]):
            print(users_list.iloc[x]["username"])
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
        #CRIA USUÁRIO
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_card():
    loop = True
    while loop:
        print(config.MENU_ADMIN_CARDS_AVAIBLES)
        cards_list = Records().list_cards()
        for x in range(cards_list.shape[0]):
            print(cards_list.iloc[x]["name"])
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
        background = select_background()
        if background == 0:
            config.clear_console(1)
            return None
        border = select_border()
        if border == 0:
            config.clear_console(1)
            return None
        rarity = select_rarity()
        if rarity == 0:
            config.clear_console(1)
            return None
        album = select_album()
        if album == 0:
            config.clear_console(1)
            return None
        CardController().insert(number, image, name, background, border, rarity, album)
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_border():
    loop = True
    while loop:
        print(config.MENU_ADMIN_BORDERS_AVAIBLES)
        border_list = Records().list_borders()
        for x in range(border_list.shape[0]):
            print(border_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        print("Criação de cartas\nDurante as opções, para sair digite '0'")
        image = input("Digite o nome do arquivo de imagem da borda\n")
        if image == "0":
            config.clear_console(1)
            return None
        name = input("Digite o nome da borda\n")
        if name == "0":
            config.clear_console(1)
            return None
        rarity = select_rarity()
        if rarity == 0:
            config.clear_console(1)
            return None
        BorderController().insert(name, image, rarity)
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_background():
    loop = True
    while loop:
        print(config.MENU_ADMIN_BACKGROUND_AVAIBLES)
        background_list = Records().list_background()
        for x in range(background_list.shape[0]):
            print(background_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        print("Criação de borda\nDurante as opções, para sair digite '0'")
        image = input("Digite o nome do arquivo de imagem do background\n")
        if image == "0":
            config.clear_console(1)
            return None
        name = input("Digite o nome do background\n")
        if name == "0":
            config.clear_console(1)
            return None
        rarity = select_rarity()
        if rarity == 0:
            config.clear_console(1)
            return None
        BackgroundController().insert(name, image, rarity_id=rarity)
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_tag():
    loop = True
    while loop:
        print(config.MENU_ADMIN_TAG_AVAIBLES)
        tag_list = Records().list_tags()
        for x in range(tag_list.shape[0]):
            print(tag_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        print("Criação de tag\nDurante as opções, para sair digite '0'")
        name = input("Digite o nome da tag\n")
        if name == "0":
            config.clear_console(1)
            return None
        print(TagController().insert(name).to_string())
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_rarity():
    controller = RarityController()
    loop = True
    while loop:
        print(config.MENU_ADMIN_RARITY_AVAIBLES)
        rarity_list = Records().list_rarity()
        for x in range(rarity_list.shape[0]):
            print(rarity_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        print("Criação de raridade\nDurante as opções, para sair digite '0'")
        name = input("Digite o nome da raridade\n")
        if name == "0":
            config.clear_console(1)
            return None
        tier = Records().list_rarity().iloc[-1]["tier"]
        controller.insert(name, tier)
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_border_tag():
    loop = True
    while loop:
        print(config.MENU_ADMIN_BORDER_TAG_AVAIBLES)
        border_tag_list = Records().list_border_tag()
        for x in range(border_tag_list.shape[0]):
            print("Border_Name: ", Records().show_border(str(border_tag_list.iloc[x]["border_id"])).iloc[0]["name"], "| Tag_Name: ", Records().show_tag(str(border_tag_list.iloc[x]["tag_id"])).iloc[0]["name"])
        print(config.MENU_SPLIT)
        print("Criação de border tag\nDurante as opções, para sair digite '0'")
        border = select_border()
        config.clear_console(1)
        tag = select_tag()
        config.clear_console(1)
        #CRIA BORDER TAG
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_card_tag():
    loop = True
    while loop:
        print(config.MENU_ADMIN_CARD_TAG_AVAIBLES)
        card_tag_list = Records().list_card_tag()
        for x in range(card_tag_list.shape[0]):
            print("Card_Name: ", Records().show_card(str(card_tag_list.iloc[x]["card_id"])).iloc[0]["name"], "| Tag_Name: ", Records().show_tag(str(card_tag_list.iloc[x]["tag_id"])).iloc[0]["name"])
        print(config.MENU_SPLIT)
        print("Criação de card tag\nDurante as opções, para sair digite '0'")
        card = select_card()
        config.clear_console(1)
        tag = select_tag()
        config.clear_console(1)
        CardTagController().insert(card, tag)
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_background_tag():
    loop = True
    while loop:
        print(config.MENU_ADMIN_BACKGROUND_TAG_AVAIBLES)
        background_tag_list = Records().list_background_tag()
        for x in range(background_tag_list.shape[0]):
            print("Background_Name: ", Records().show_background(str(background_tag_list.iloc[x]["background_id"])).iloc[0]["name"], "| Tag_Name: ", Records().show_tag(str(background_tag_list.iloc[x]["tag_id"])).iloc[0]["name"])
        print(config.MENU_SPLIT)
        print("Criação de background tag\nDurante as opções, para sair digite '0'")
        background = select_background()
        tag = select_tag()
        #CRIA BACKGROUND TAG
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def create_user_card():
    loop = True
    while loop:
        print(config.MENU_ADMIN_USER_CARD_AVAIBLES)
        user_card_list = Records().list_user_card()
        for x in range(user_card_list.shape[0]):
            print("User_Name: ", Records().show_user(str(user_card_list.iloc[x]["user_id"])).iloc[0]["username"], "| Card_Name: ", Records().show_card(str(user_card_list.iloc[x]["card_id"])).iloc[0]["name"])
        print(config.MENU_SPLIT)
        print("Criação de user card\nDurante as opções, para sair digite '0'")
        user = select_user()
        card = select_card()
        #CRIA USER CARD
        if menu_continue() == 2:
            return None
        config.clear_console(1)

def select_background():
    print(config.MENU_ADMIN_BACKGROUND_AVAIBLES)
    background_list = Records().list_background()
    for x in range(background_list.shape[0]):
        print(f"{x + 1} - " + background_list.iloc[x]["name"])
    print(config.MENU_SPLIT)
    background = input("Digite o numero do background que deseja selecionar ou 0 para sair\n")
    loop = True
    while loop:
        background_verification = Records().show_background(background)
        if id == "0":
            loop = False
            config.clear_console(1)
            return 0
        elif not background_verification.empty:
            config.clear_console(1)
            return background
        while background_verification.empty:
            background = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

def select_border():
    print(config.MENU_ADMIN_BORDERS_AVAIBLES)
    border_list = Records().list_borders()
    for x in range(border_list.shape[0]):
        print(f"{x + 1} - " + border_list.iloc[x]["name"])
    print(config.MENU_SPLIT)
    border = input("Digite o número da borda que deseja selecionar ou 0 para sair\n")
    loop = True
    while loop:
        border_verification = Records().show_border(border)
        if border == "0":
            loop = False
            config.clear_console(1)
            return 0
        elif not border_verification.empty:
            config.clear_console(1)
            return border
        while border_verification.empty:
            border = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

def select_rarity():
    print(config.MENU_ADMIN_RARITY_AVAIBLES)
    rarity_list = Records().list_rarity()
    for x in range(rarity_list.shape[0]):
        print(f"{x + 1} - " + rarity_list.iloc[x]["name"])
    print(config.MENU_SPLIT)
    rarity = input("Digite o número da raridade que deseja selecionar ou 0 para sair\n")
    loop = True
    while loop:
        rarity_verification = Records().show_rarity(rarity)
        if rarity == "0":
            loop = False
            config.clear_console(1)
            return 0
        elif not rarity_verification.empty:
            config.clear_console(1)
            print(rarity)
            return rarity
        while rarity_verification.empty:
            rarity = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

def select_album():
    print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
    albuns_list = Records().list_albuns()
    for x in range(albuns_list.shape[0]):
        print(f"{x + 1} - " + albuns_list.iloc[x]["title"])
    print(config.MENU_SPLIT)
    album = input("Digite o número do album que deseja selecionar ou 0 para sair\n")
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

def select_card():
    print(config.MENU_ADMIN_CARDS_AVAIBLES)
    card_list = Records().list_cards()
    for x in range(card_list.shape[0]):
        print(f"{x + 1} - " + card_list.iloc[x]["name"])
    print(config.MENU_SPLIT)
    card = input("Digite o número da carta que deseja selecionar ou 0 para sair\n")
    loop = True
    while loop:
        card_verification = Records().show_card(card)
        if card == "0":
            loop = False
            config.clear_console(1)
            return 0
        elif not card_verification.empty:
            config.clear_console(1)
            return card
        while card_verification.empty:
            card = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

def select_user():
    print(config.MENU_ADMIN_USERS_AVAIBLES)
    user_list = Records().list_users()
    for x in range(user_list.shape[0]):
        print(f"{x + 1} - " + user_list.iloc[x]["username"])
    print(config.MENU_SPLIT)
    user = input("Digite o número do usuário que deseja selecionar ou 0 para sair\n")
    loop = True
    while loop:
        user_verification = Records().show_user(user)
        if user == "0":
            loop = False
            config.clear_console(1)
            return 0
        elif not user_verification.empty:
            config.clear_console(1)
            return user
        while user_verification.empty:
            user = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

def select_tag():
    print(config.MENU_ADMIN_TAG_AVAIBLES)
    tag_list = Records().list_tags()
    for x in range(tag_list.shape[0]):
        print(f"{x + 1} - " + tag_list.iloc[x]["name"])
    print(config.MENU_SPLIT)
    tag = input("Digite o número da tag que deseja selecionar ou 0 para sair\n")
    loop = True
    while loop:
        tag_verification = Records().show_tag(tag)
        if tag == "0":
            loop = False
            config.clear_console(1)
            return 0
        elif not tag_verification.empty:
            config.clear_console(1)
            return tag
        while tag_verification.empty:
            tag = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            break

def menu_continue():
    config.clear_console(1)
    print(config.MENU_ADMIN_CREATE_RECORDS_CONTINUE)
    selection = str(input("Insira sua opção\n"))
    if selection == "2":
        config.clear_console(1)
        return 2
    config.clear_console(1)