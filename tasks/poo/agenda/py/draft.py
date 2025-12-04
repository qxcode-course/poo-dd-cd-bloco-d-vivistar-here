from typing import List

class Fone:
    def __init__(self, id: str, number: str):
        self.__id = id
        self.__number = number

    def getId(self):
        return self.__id

    def getNumber(self):
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
        self.__fones: List[Fone] = []
        self.__favorited = False

    def addFone(self, id: str, number: str) -> None:
        fone = Fone(id, number)
        if fone.isValid():
            self.__fones.append(fone)
        else:
            print("fail: comando inexistente")

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: comando inexistente")

    def toggleFavorited(self) -> None:
        self.__favorited = not self.__favorited

    def isFavorited(self) -> bool:
        return self.__favorited

    def getFones(self):
        return self.__fones

    def getName(self):
        return self.__name

    def setName(self, name: str) -> None:
        self.__name = name

    def __str__(self) -> str:
        prefix = "@ " if self.__favorited else "- "
        phones_str = ", ".join([f"{i}:{str(fone)}" for i, fone in enumerate(self.__fones)])
        return f"{prefix}{self.__name} [{phones_str}]"

class Agenda:
    def __init__(self):
        self.__contacts: List[Contact] = []

    def __findPosByName(self, name: str) -> int:
        for i, contact in enumerate(self.__contacts):
            if contact.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: List[Fone]):
        pos = self.__findPosByName(name)
        if pos != -1:
            contact = self.__contacts[pos]
            for fone in fones:
                contact.addFone(fone.getId(), fone.getNumber())
        else:
            novo = Contact(name)
            for fone in fones:
                novo.addFone(fone.getId(), fone.getNumber())
                self.__contacts.append(novo)
                self.__contacts.sort(key=lambda contact: contact.getName())

    def getContact(self, name: str):
        for contact in self.__contacts:
            if contact.getName() == name:
                return contact 
        return None

    def rmContact(self, name: str):
        pos = self.__findPosByName(name)
        if pos == -1:
            print("fail: contato não existe")
        else:
            self.__contacts.pop(pos)

    def search(self, pattern: str) -> List[Contact]:
        result = []
        pattern = pattern.lower()
        for contact in self.__contacts:
            name_match = pattern in contact.getName().lower()
            fone_match = False

            for fone in contact.getFones():
                if pattern in fone.getId().lower() or pattern in fone.getNumber().lower():
                    fone_match = True
                    break
            
            if name_match or fone_match:
                result.append(contact)
        return result
    
    def getFavorited(self):
        result = []
        for contact in self.__contacts:
            if contact.isFavorited():
                result.append(contact)
        return result

    def getContacts(self):
        return self.__contacts

    def __str__(self) -> str:
        result = []
        for contact in self.__contacts:
            result.append(str(contact))
        return "\n".join(result)

def main():
    agenda = None
    while True:
        line = input()
        args = line.split(" ")
        print(f"${line}")

        if args[0] == "end":
            break
        
        elif args[0] == "init":
            agenda = Agenda()

        elif args[0] == "add":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            name = args[1]
            fones = []
            for fone in args[2:]:
                if ":" not in fone:
                    print("fail: fone inválido")
                    continue
                id, number = fone.split(":")
                fones.append(Fone(id, number))

            agenda.addContact(name, fones)

        elif args[0] == "show":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            print(agenda)

        elif args[0] == "rm":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            name = args[1]
            agenda.rmContact(name)

        elif args[0] == "rmFone":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)

            if contact is None:
                print("fail: contato não existe")
                continue
            contact.rmFone(index)

        elif args[0] == "search":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue

            pattern = args[1]
            result = agenda.search(pattern)

            for contact in result:
                print(contact)

        elif args[0] == "fav":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            name = args[1]
            contact = agenda.getContact(name)

            if contact is None:
                print("fail: contato não existe")
                continue
            
            contact.toggleFavorited()

        elif args[0] == "unfav":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            name = args[1]
            contact = agenda.getContact(name)

            if contact is None:
                print("fail: contato não existe")
                continue
            contact.toggleFavorited()

        elif args[0] == "showFav":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            
            for contact in agenda.getFavorited():
                print(contact)

        else:
                print("fail: comando inválido")

main()