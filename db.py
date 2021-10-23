from typing import List

from table import Table


class Db:
    group: str
    description: str
    tables: List[Table] = []

    def __init__(self) -> None:
        pass

    def setGroup(self, group: str) -> None:
        self.group = "group: " + group

    def setDesctiption(self, description: str) -> None:
        self.description = "description: " + description

    def addTable(self, tab: list) -> None:
        self.tables.append(tab)

    def getDb(self) -> None:
        print(self.group)
        print(self.description)

        for items in self.tables:
            print(items.attributes)
            print(*items.tuples, sep='\n')
