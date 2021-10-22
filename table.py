from typing import List


class Table:
    
    tuples: List[List[str]] = []
    attribute: List[str] = []

    def __init__(self):
        pass
    
    def addTuple(self, row: list) -> None:
        
        self.tuples.append(row)

    def setAttributes(self, row: list) -> None:

        self.attribute=row


