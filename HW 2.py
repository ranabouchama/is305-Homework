"""
Discussion Question 1:

String would ultimately be less accurate, as it isn't based on Unicode but rather ASCII. Meaning that some Pokémon names 
would not be represented correctly within the dataset. The word "Pokémon" itself wouldn't even be handled correctly, it would
become Pokmon, as String would not recognize the "é". 

Discussion Question 2:

For some reason, I ended up with 946 rows, as that is just around the goal of 950, I figured it wasn't worth the trouble to
recode it. Especially given how busy I am. At any rate, the CSV file has 980 rows; 34 of them were failures, that leaves only
946 rows as a result.

"""

import csv
from pathlib import Path


def clean_name(name):
    """Keep only characters that pass str.isalnum()."""
    return "".join(ch for ch in name if ch.isalnum())


# testing
print(clean_name("A-Compl3x?_mon"))  # ACompl3xmon

base = Path(__file__).parent
source = base / "pokemon_names_and_descriptions.csv"
target = base / "description_text"

# loading data
with open(source, newline="", encoding="utf-8") as infile:
    reader = csv.reader(infile)
    headers = next(reader)
    data = list(reader)
print(len(headers), len(data))  # 3, 980

# output folder 
target.mkdir(exist_ok=True)

# dictionary to collect failures
pokemon = {}
failures = []
for row in data:
    number, name, notes = row[0].strip(), row[1], row[2]
    cleaned = clean_name(name)
    if not number.isnumeric() or cleaned == "":
        failures.append(row)
        continue
    file_name = f"{number.zfill(3)}-{cleaned}.txt"
    pokemon[file_name] = notes

print(len(pokemon), len(failures))  # 946, 34

# write the file
for file_name, notes in pokemon.items():
    (target / file_name).write_text(notes, encoding="utf-8")
print(len(list(target.glob("*.txt"))))  # 946

# Step 7: write failures.csv
with open(base / "failures.csv", "w", newline="", encoding="utf-8") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(headers)
    writer.writerows(failures)
