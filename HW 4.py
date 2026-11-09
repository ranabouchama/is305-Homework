import csv
import string
from collections import Counter

# lab 4 ngram

def ngram_letters(name, num):
    name = name.lower()
    nameparts = [n.strip(string.punctuation) for n in name.split()]

    grams = []
    if len(nameparts) > 1:
        for part in nameparts:
            grams += ngram_letters(part,num)
    else:
        for i in range(len(name)):
            if i + num > len(name):
                break
            grams.append(name[i:i + num])
    return grams

critters = ["Pikachu", "Mr. Mime", "Mega Charizard"]

parts = []

for name in critters:
    parts += ngram_letters(name, 2)

print(parts)


print(ngram_letters("pikachu", 2))

# load pokemon names
pokemon_names = []
with open("pokemon_names_and_descriptions__2_.csv", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        name = row[1].strip()
        if name != "":
            pokemon_names.append(name)

# load big data names
bigdata_names = []
with open("bigdata.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line != "":
            bigdata_names.append(line)

# create unique versions
pokemon_names = list(set(pokemon_names))
bigdata_names = list(set(bigdata_names))

print(len(pokemon_names))
print(pokemon_names[:5])
print(len(bigdata_names))
print(bigdata_names[:5])

# collect letter pairs
duos = []
for name in pokemon_names:
    duos += ngram_letters(name, 2)
for name in bigdata_names:
    duos += ngram_letters(name, 2)

unique_duos = list(set(duos))
print("there are", len(duos), "individual pairs")
print(duos[:10])
print("there are", len(unique_duos), "unique letter pairs")

# headers
headers = ["name"] + unique_duos + ["type"]
print("uniques are", len(unique_duos), "but headers is", len(headers))
print(headers[0:3], "...", headers[-3:])

# counts
all_counted_parts = []
for name in pokemon_names:
    entity_results = dict(Counter(ngram_letters(name, 2)))
    entity_results["name"] = name
    entity_results["type"] = "pokemon"
    all_counted_parts.append(entity_results)

for name in bigdata_names:
    entity_results = dict(Counter(ngram_letters(name, 2)))
    entity_results["name"] = name
    entity_results["type"] = "big_data"
    all_counted_parts.append(entity_results)

print(len(all_counted_parts))
print(all_counted_parts[:2])

# sparse rows
bag = []
for entity in all_counted_parts:
    row = [0] * len(headers)
    for key in entity:
        row[headers.index(key)] = entity[key]
    bag.append(row)

print(len(bag))
print(bag[0])

# write csv
with open("pokemon_bigdata_bow.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(bag)
