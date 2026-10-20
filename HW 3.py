import csv

# read in the CSV (standard boilerplate)
with open("pokemon_names_and_descriptions.csv", encoding="utf-8") as file:
    reader = csv.reader(file)
    headers = next(reader)      
    data = list(reader)         

# step 1: collect the index positions
missing = []
for i, row in enumerate(data):
    if row[0] == "" and row[1] == "":
        missing.append(i)
print("Step 1:", len(missing), missing)

# step 2: cluster empty rows
clusters = []
for i, pos in enumerate(missing):
    if i > 0 and pos == missing[i - 1] + 1:
        clusters[-1].append(pos)     
    else:
        clusters.append([pos])       # start a new cluster
print("Step 2:", len(clusters), clusters)

# step 3: add the index of the row with the name to each cluster
for cluster in clusters:
    cluster.insert(0, cluster[0] - 1)
print("Step 3:", clusters)

# step 4: access the content via the index positions
print("Step 4:")
for cluster in clusters:
    for pos in cluster:
        print(data[pos])

# step 5: extract and populate the new content
print("Step 5:")
for cluster in clusters:
    dex = data[cluster[0]][0]
    name = data[cluster[0]][1]
    for pos in cluster[1:]:
        data[pos][0] = dex
        data[pos][1] = name
    for pos in cluster:
        print(data[pos])

print(data[349:356])

# step 6: write out the new version
with open("updated_pokemon_names_and_descriptions.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)
