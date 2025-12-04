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
        return self.__number.isdigit()

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
            print("fail: fone invalido")

    def rmFone(self, index: int) -> None:
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
        else:
            print("fail: indice invalido")

    def toogleFavorited(self):
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
        fones_str = ", ".join([f"{i}:{fone}" for i, fone in enumerate(self.__fones)])
        return f"{fav} {self.__name} [{fones_str}]"

class Agenda:
    def __init__(self):
        self.__contacts: List[Contact] = []

    def __findPosByName(self, name: str) -> int:
        for i, contact in enumerate(self.__contacts):
            if contact.getName() == name:
                return i
        return -1

    def addContact(self, name: str, fones: List[List[str]]):
        pos = self.__findPosByName(name)
        if pos == -1:
            contact = Contact(name)
            for id, number in fones:
                contact.addFone(id, number)
            self.__contacts.append(contact)
            self.__contacts.sort(key=lambda contact: contact.getName())
        else:
            contact = self.__contacts[pos]
            for id, number in fones:
                contact.addFone(id, number)
            

    def getContact(self, name: str):
        pos = self.__findPosByName(name)
        return self.__contacts[pos] if pos != -1 else None

    def rmContact(self, name: str):
        pos = self.__findPosByName(name)
        if pos != -1:
            self.__contacts.pop(pos)
        else:
            print("fail: contato nao existe")
            

    def search(self, pattern: str) -> List[Contact]:
        result: List[Contact] = []
        pattern = pattern.lower()
        for contact in self.__contacts:
            if pattern in contact.getName().lower():
                results.append(contact)
                continue
            for fone in contact.getFones():
                if pattern in fone.getId().lower() or pattern in fone.getNumber():
                    result.append(contact)
                    break
        return result
    
    def getFavorited(self) -> List[Contact]:
        return [contact for contact in self.__contacts if contact.isFavorited()]

    def getContacts(self) -> List[Contact]:
        return self.__contacts

    def __str__(self):
        if not self.__contacts:
            return ""
        return "\n".join(str(contact) for contact in self.__contacts)

def main():
    agenda = Agenda()
    while True:
        line = input()
        args = line.split(" ")
        print("$" + line)

        if args[0] == "end":
            break

        elif args[0] == "add":
            name = args[1]
            fones: List[List[str]] = []
            for fone_str in args[2:]:
                if ":" not in fone_str:
                    print("fail: fone invalido")
                    break
                id, number = fone_str.split(":")
                fones.append([id, number])
            else:
                agenda.addContact(name, fones)

        elif args[0] == "show":
            if agenda is None:
                print("fail: agenda não inicializada")
                continue
            print(agenda)

        elif args[0] == "rm":
            name = args[1]
            agenda.rmContact(name)
        
        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)

            if contact:
                contact.rmFone(index)
            else:
                print("fail: contato nao existe")

        elif args[0] == "search":
            pattern = args[1]    
            for contact in agenda.search(pattern):
                print(contact)

        elif args[0] == "fav":
            name = args[1]
            contact = agenda.getContact(name)
            if contact:
                contact.toogleFavorited()
            else:
                print("fail: contato nao existe")

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