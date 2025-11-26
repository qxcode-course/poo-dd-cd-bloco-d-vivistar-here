class Fone:
    def __init__(self, id: str, number: str):
        self.id = id
        self.number = number

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

    