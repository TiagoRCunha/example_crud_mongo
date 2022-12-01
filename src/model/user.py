class User:
    def __init__(self, name:str=None, password:str=None, access_type:int=None):
        self.set_name(name)
        self.set_password(password)
        self.set_access_type(access_type)

    def set_name(self, name:str):
        self.name = name

    def set_password(self, password:int):
        self.password = password

    def set_access_type(self, access_type:int):
        self.access_type = access_type

    def get_name(self) -> str:
        return self.name

    def get_password(self) -> str:
        return self.password

    def get_access_type(self) -> int:
        return self.access_type