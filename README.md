# CSVtoRelaX

convert CSV file to readable RelaX format

## Usage
```
python3 main.py -i dir_path -o out_file [-g name_of_group] [-d desc]
```

## Arguments:

| Argument          | Description                     |
| ---               | ---                             |
|  -h, --help       | Show help message and exit      |
|  -i dir_path      | The directory with CSV files    |
|  -o out_file      | Path of the output file         |
|  -g name_of_group | Name of the RelaX Dataset Group |
|  -d desc          | RelaX Dataset Group description |

## Example

Directory Database: 
```
RelazioniAlgebra
```

CVS Tables: 
```
dipart.csv
dipendenti.csv
fornitori.csv
forniture.csv
parti.csv
prodotti.csv
sped_dettagli.csv
spedizioni.csv
```

Command:
```
python3 main.py -i RelazioniAlgebra/ -o RelazioniAlgebra.txt -g RelazioniAlgebra -d test_relazioni_algebra
```

Output:
```
RelazioniAlgebra.txt
```
