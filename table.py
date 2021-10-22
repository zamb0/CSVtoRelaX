class Table:
    
    tuples: list = []
    attributs: list = []

    def __init__(self):
        pass
    
    def addTuple(self, row: list) -> None:
        
        self.tuples.append(row)

    def setAttributes(self, row: list) -> None:

        self.attributs=row


