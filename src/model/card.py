class Card:
    def __init__(self, number:int=None, image:str=None, name:str=None, background:str=None, border:str=None, rarity:int=None, album:str=None):
        self.set_number(number)
        self.set_image(image)
        self.set_name(name)
        self.set_background(background)
        self.set_border(border)
        self.set_rarity(rarity)
        self.set_album(album)

    def set_number(self, number:str):
        self.number = number

    def set_image(self, image:str):
        self.image = image

    def set_name(self, name:str):
        self.name = name

    def set_background(self, background:str):
        self.background = background

    def set_border(self, border:str):
        self.border = border

    def set_rarity(self, rarity:int):
        self.rarity = rarity

    def set_album(self, album:str):
        self.album = album

    def get_number(self) -> int:
        return self.number

    def get_image(self) -> str:
        return self.image

    def set_name(self) -> str:
        return self.name

    def set_background(self) -> str:
        return self.background

    def set_border(self) -> str:
        return self.border

    def set_rarity(self) -> int:
        return self.rarity

    def set_album(self) -> str:
        return self.album
