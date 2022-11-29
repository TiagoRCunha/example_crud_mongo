from controller.controller_rarity import RarityController
from controller.controller_tag import TagController
import utils.config as config
from utils.records import Records
from controller.controller_border import BorderController

def remove_album():
    loop = True
    while loop:
        print(config.MENU_ADMIN_ALBUNS_AVAIBLES)
        albuns_list = Records().list_albuns()
        for x in range(albuns_list.shape[0]):
            print(f"{x + 1} - " + albuns_list.iloc[x]["title"])
        print(config.MENU_SPLIT)
        id = input("Digite o número do album que deseja remover ou 0 para sair\n")
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
            if menu_confirm() == 1:
                #REMOVER ALBUM
                config.clear_console(1)
                if menu_continue() == 2:
                    return None


def remove_user():
    loop = True
    while loop:
        print(config.MENU_ADMIN_USERS_AVAIBLES)
        users_list = Records().list_users()
        for x in range(users_list.shape[0]):
            print(f"{x + 1} - " + users_list.iloc[x]["username"])
        print(config.MENU_SPLIT)
        id = input("Digite o número do usuário que deseja remover ou 0 para sair\n")
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
            if menu_confirm() == 1:
                #REMOVER USUARIO
                config.clear_console(1)
                if menu_continue() == 2:
                    return None
        

def remove_card():
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
            if menu_confirm() == 1:
                #REMOVER CARTA
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def remove_border():
    loop = True
    while loop:
        print(config.MENU_ADMIN_BORDERS_AVAIBLES)
        border_list = Records().list_borders()
        for x in range(border_list.shape[0]):
            print(f"{x + 1} - " + border_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da borda que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_border(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_border(id)
        if not id_verification.empty:
            if menu_confirm() == 1:
                BorderController().delete(id)
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def remove_background():
    loop = True
    while loop:
        print(config.MENU_ADMIN_BACKGROUND_AVAIBLES)
        background_list = Records().list_background()
        for x in range(background_list.shape[0]):
            print(f"{x + 1} - " + background_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número do background que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_background(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_background(id)
        if not id_verification.empty:
            if menu_confirm() == 1:
                #REMOVER BACKGROUND
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def remove_tag():
    loop = True
    while loop:
        print(config.MENU_ADMIN_TAG_AVAIBLES)
        tag_list = Records().list_tags()
        for x in range(tag_list.shape[0]):
            print(f"{x + 1} - " + tag_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da tag que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_tag(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_tag(id)
        if not id_verification.empty:
            if menu_confirm() == 1:
                print(TagController().delete(id))
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def remove_rarity():
    controller = RarityController()
    loop = True
    while loop:
        print(config.MENU_ADMIN_RARITY_AVAIBLES)
        rarity_list = Records().list_rarity()
        for x in range(rarity_list.shape[0]):
            print(f"{x + 1} - " + rarity_list.iloc[x]["name"])
        print(config.MENU_SPLIT)
        id = input("Digite o número da raridade que deseja alterar ou 0 para sair\n")
        id_verification = Records().show_rarity(id)
        if id == "0":
            config.clear_console(1)
            return None
        while id_verification.empty:
            id = input("\nOpção inválida, digite novamente ou 0 para sair\n")
            if id == "0":
                config.clear_console(1)
                return None
            id_verification = Records().show_rarity(id)
        if not id_verification.empty:
            if menu_confirm() == 1:
                controller.delete(id)
                config.clear_console(1)
                if menu_continue() == 2:
                    return None

def remove_border_tag():
    print(config.MENU_ADMIN_BORDER_TAG_AVAIBLES)
    border_tag_list = Records().list_border_tag()
    for x in range(border_tag_list.shape[0]):
        print(f"{x + 1} - ", "Border_Name: ", Records().show_border(str(border_tag_list.iloc[x]["border_id"])).iloc[0]["name"], "| Tag_Name: ", Records().show_tag(str(border_tag_list.iloc[x]["tag_id"])).iloc[0]["name"])
    print(config.MENU_SPLIT)
    border_tag = int(input("Digite o número da border tag que deseja remover ou 0 para sair\n"))
    if border_tag == 0:
        config.clear_console(1)
        return None
    border_tag -= 1
    while border_tag >= border_tag_list.shape[0]:
        border_tag = int(input("Número da border tag inválido, insira novamente ou 0 para sair\n"))
        if border_tag == 0:
            config.clear_console(1)
            return None
        border_tag -= 1
    border_id = str(border_tag_list.iloc[border_tag]["border_id"])
    tag_id = str(border_tag_list.iloc[border_tag]["tag_id"])
    if menu_confirm() == 1:
        #REMOVE BORDER TAG USANDO AS ID ACIMA
        config.clear_console(1)
        if menu_continue() == 2:
            return None

def remove_card_tag():
    print(config.MENU_ADMIN_CARD_TAG_AVAIBLES)
    card_tag_list = Records().list_card_tag()
    for x in range(card_tag_list.shape[0]):
        print(f"{x + 1} - ", "Card_Name: ", Records().show_card(str(card_tag_list.iloc[x]["card_id"])).iloc[0]["name"], "| Tag_Name: ", Records().show_tag(str(card_tag_list.iloc[x]["tag_id"])).iloc[0]["name"])
    print(config.MENU_SPLIT)
    card_tag = int(input("Digite o número da card tag que deseja remover ou 0 para sair\n"))
    if card_tag == 0:
        config.clear_console(1)
        return None
    card_tag -= 1
    while card_tag >= card_tag_list.shape[0]:
        card_tag = int(input("Número da card tag inválido, insira novamente ou 0 para sair\n"))
        if card_tag == 0:
            config.clear_console(1)
            return None
        card_tag -= 1
    card_id = str(card_tag_list.iloc[card_tag]["card_id"])
    tag_id = str(card_tag_list.iloc[card_tag]["tag_id"])
    if menu_confirm() == 1:
        #REMOVE CARD TAG USANDO AS ID ACIMA
        config.clear_console(1)
        if menu_continue() == 2:
            return None

def remove_background_tag():
    print(config.MENU_ADMIN_BACKGROUND_TAG_AVAIBLES)
    background_tag_list = Records().list_background_tag()
    for x in range(background_tag_list.shape[0]):
        print(f"{x + 1} - ", "Background_Name: ", Records().show_background(str(background_tag_list.iloc[x]["background_id"])).iloc[0]["name"], "| Tag_Name: ", Records().show_tag(str(background_tag_list.iloc[x]["tag_id"])).iloc[0]["name"])
    print(config.MENU_SPLIT)
    background_tag = int(input("Digite o número do background tag que deseja remover ou 0 para sair\n"))
    if background_id == 0:
        config.clear_console(1)
        return None
    background_id -= 1
    while background_tag >= background_tag_list.shape[0]:
        background_tag = int(input("Número do background tag inválido, insira novamente ou 0 para sair\n"))
        if background_tag == 0:
            config.clear_console(1)
            return None
        background_tag -= 1
    background_id = str(background_tag_list.iloc[background_tag]["background_id"])
    tag_id = str(background_tag_list.iloc[background_tag]["tag_id"])
    if menu_confirm() == 1:
        #REMOVE BACKGROUND TAG USANDO AS ID ACIMA
        config.clear_console(1)
        if menu_continue() == 2:
            return None

def remove_user_card():
    print(config.MENU_ADMIN_USER_CARD_AVAIBLES)
    user_card_list = Records().list_user_card()
    for x in range(user_card_list.shape[0]):
        print(f"{x + 1} - ", "User_Name: ", Records().show_user(str(user_card_list.iloc[x]["user_id"])).iloc[0]["username"], "| Card_Name: ", Records().show_card(str(user_card_list.iloc[x]["card_id"])).iloc[0]["name"])
    print(config.MENU_SPLIT)
    user_card = int(input("Digite o número da user card que deseja remover ou 0 para sair\n"))
    if user_card == 0:
        config.clear_console(1)
        return None
    user_card -= 1
    while user_card >= user_card_list.shape[0]:
        user_card = int(input("Número da user card inválido, insira novamente ou 0 para sair\n"))
        if user_card == 0:
            config.clear_console(1)
            return None
        user_card -= 1
    user_id = str(user_card_list.iloc[user_card]["user_id"])
    card_id = str(user_card_list.iloc[user_card]["card_id"])
    if menu_confirm() == 1:
        #REMOVE USER CARD USANDO AS ID ACIMA
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