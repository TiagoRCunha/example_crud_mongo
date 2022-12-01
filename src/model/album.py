class Album:
    def __init__(self, title:str=None, page_count:int=None, card_count:int=None, description:str=None):
        self.set_title(title)
        self.set_page_count(page_count)
        self.set_card_count(card_count)
        self.set_description(description)

    def set_title(self, title:str):
        self.title = title

    def set_page_count(self, page_count:int):
        self.page_count = page_count

    def set_card_count(self, card_count:int):
        self.card_count = card_count

    def set_description(self, description:str):
        self.description = description

    def get_title(self) -> str:
        return self.title

    def get_page_count(self) -> int:
        return self.page_count

    def get_card_count(self) -> int:
        return self.card_count

    def get_description(self) -> str:
        return self.description