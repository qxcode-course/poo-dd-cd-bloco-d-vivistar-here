class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId(self):
        return self.id

    def getNumber(self):
        return self.number

    def isValid(self) -> bool:
        validos = "0123456789"
        for c in self.number:
            if c not in validos:
                return False
            return True

    def __str__(self):
        return f"{self.id}:{self.number}"

class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited: bool = favorited

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.fone.append(fone)
        else:
            print("fail: comando inexistente")

    