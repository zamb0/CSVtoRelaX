from typing import List


class Table:

    name: str
    tuples: list = []
    attributes: list = []

    def __init__(self):
        pass
    
    def addTuple(self, row: list) -> None:
        
        self.tuples.append(row)

    def setAttributes(self, row: list) -> None:

        self.attributes=row


