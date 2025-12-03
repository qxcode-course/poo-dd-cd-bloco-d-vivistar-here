class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId(self, id: str):
        return self.__id

    def getNumber(self, number: str):
        return self.__number

    def isValid(self) -> bool:
        validos = "0123456789"
        for c in self.__number:
            if c not in validos:
                return False
            return True

    def __str__(self):
        return f"{self.__id}:{self.__number}"

class Contact:
    def __init__(self, name: str):
        self.__name = name
        self.__fones: list[Fone] = []
        self.__favorited: bool = favorited

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.fones.append(fone)
        else:
            print("fail: comando inexistente")

    def rmFone(self, index: int) -> None:
        if 0 < index < len(self.__fones):
            self.fones.pop(index)
        else:
            print("fail: comando inexistente")

    def toggleFavorited(self) -> None:
        self.favorite = not self.favorite

    def isFavorited(self) -> bool:
        return self.favorited

    def getFones(self) -> list:
        return self.__fones

    def getName(self, name: str):
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        prefix = "@ " if self.favorited else "- "
        phones_str = ", ".join([f"{i}:{str(fone)}" for i, fone in enumerate(self.__fones)])
        return f"{prefix}{self.__name} [{phones_str}]"

class Agenda:
    def __init__(self):
        self.__contacts = []

    def __findPosByName(self, name: str) -> int:
        for i in range(len(self.__contacts)):
            contact = self.__contacts[i]
            if contact.getName() == name:
                return id
        return -1

    def addContact(self, name: str, fones: list):
        pos = self.__findPosByName(name)
        if pos != -1:
            contact = self.__contacts[pos]
            for fone in fones:
                contact.addFone(fone.__id, fone.__number)
        else:
            novo = Contact(name)
            for fone in fones:
                novo.addFOne(fone.__id, fone.__number)
                self.__contacts.append(novo)
                self.__contacts.sort(key=lambda contact: contact.getName())

        def getContact(self, name: str):
            for contact in self.__contacts:
                if contact.getName() == name:
                    return contact 
            return None

        def rmContact(self, name: str):
            