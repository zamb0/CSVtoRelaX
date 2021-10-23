import argparse
import csv
from os import listdir
from os.path import isfile, join, basename

from table import Table


def file_to_table(file_path: str) -> Table:
    table: Table = Table()
    table.name = basename(file_path).split(".")[0]
    with open(file_path) as csv_file:
        rows = [row for row in csv.reader(csv_file)]
        table.attributes = rows[0]
        table.tuples = rows[1:]
    return table


def format_table(table: Table) -> str:
    return f"{table.name} = {{\n" \
           + ", ".join(table.attributes) \
           + "\n\n" \
           + "\n".join(", ".join(map(format_tuple, tuple)) for tuple in table.tuples) \
           + "\n}\n"


def format_tuple(value: str) -> str:
    if value.lower() == "null":
        return "null"
    elif value.isnumeric():
        return value
    else:
        return f"'{value}'"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Converts CSV files to RelaX Dataset.')
    parser.add_argument('-i', metavar='dir_path', required=True, dest='input', help='The directory with CSV files')
    parser.add_argument('-o', metavar='out_file', required=True, dest='output', help='Path of the output file')
    parser.add_argument('-g', metavar='name_of_group', dest='group', help='Name of the RelaX Dataset Group')
    parser.add_argument('-d', metavar='desc', dest='desc', help='RelaX Dataset Group description')

    args = parser.parse_args()

    files_path = [join(args.input, file) for file in listdir(args.input) if isfile(join(args.input, file))]
    tables = [file_to_table(file) for file in files_path]
    formatted_rels = [format_table(table) for table in tables]

    with open(args.output, 'w') as output_file:
        output = "group: " \
                 + (f"{args.group}" if args.group is not None else basename(args.output).split(".")[0]) \
                 + "\n" \
                 + (f"description: {args.desc}\n" if args.desc is not None else "") \
                 + "\n" \
                 + "\n".join(formatted_rels)
        output_file.write(output)
