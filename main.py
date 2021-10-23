# Fabio Zamboni & Davide Ferrari
# elaboratore file csv
# per il mitico Ferretti


## TODO
## command line interface
## parsing of csv file
## print to a txt file
## NULL management

import csv
from db import Db
from table import Table
import argparse

db: Db = Db()

def loadFile(filename: str) -> list:
    tmp: list = []

    with open(filename, newline='') as csvfile:

        spamreader = csv.reader(csvfile)

        for row in spamreader:
            #addQuotesToString(0, row) #<-----------   add Quotes to String element
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

def addQuotesToString(i: int, row: str) -> None:

    i=0
    for string in row:
        if(string.isnumeric()):
            pass
        else:
            row[i]="'"+string+"'"
        i+=1

db.addTable(elabFile(loadFile("RelazioniAlgebra/spedizioni.csv")))
db.setGroup("Ciao")
db.setDesctiption("Test")
#db.getDb()