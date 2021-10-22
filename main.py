#Fabio Zamboni
#elaboratore file csv
#per il mitico Ferretti

import csv
from db import Db
from table import Table

db: Db = Db()


def loadFile(filename: str) -> list:
    tmp: list = []
    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            tmp.append(', '.join(row))
    return tmp

def elabFile(table: list) -> Table:
    i: int = 0
    t: Table = Table() 

    for items in table:
        if(i==0):
            t.setAttributes(items)
            i=1
        else:
            t.addTuple(items)
    return t

db.addTable(elabFile(loadFile("RelazioniAlgebra/spedizioni.csv")))
db.setGroup("Ciao")
db.setDesctiption("Test")
db.getDb()