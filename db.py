from table import Table


class Db:

    group: str 
    description: str
    tables: list = []

    def __init__(self) -> None:
        pass

    def setGroup(self, group) -> None:
        self.group = "group: "+group

    def setDesctiption(self, description) -> None:
        self.description = "description: "+description

    def addTable(self, tab: list) -> None:
        self.tables.append(tab)

    def getDb(self) -> None:
        
        print(self.group)
        print(self.description)

        for items in self.tables:
            print(items.attributs)
            print(*items.tuples, sep='\n')