# variables and row data from assignment
top_header = ['', '', 'Name', '', 'National Pokédex\nnumber', 'Type(s)', '', 'Evolves from', 'Evolves into', 'Notes']
bottom_header = ['','Generation', 'English', 'Japanese', '', 'Primary', 'Secondary', '', '', '']

# assert lists same length
assert len(top_header) == len(bottom_header), "Error: Header lists must be of the same length."

def combine_headers(top_str, bottom_str):
    assert isinstance(top_str, str), "Error: top_str must be a string string type."
    assert isinstance(bottom_str, str), "Error: bottom_str must be a string string type."
    # rules: single else if/elif block
    if bottom_str != "" and top_str != "":
        selection = bottom_str
    elif bottom_str != "" and top_str == "":
        selection = bottom_str
    elif top_str != "" and bottom_str == "":
        selection = top_str
    else:
        selection = "MissingLabel"
        
    return selection


# ver 1 loop look-up
print("This is the First Version")
new_headers_index = []
for index in range(len(top_header)):
    selected_header = combine_headers(top_header[index], bottom_header[index])
    new_headers_index.append(selected_header)

print(new_headers_index)


# ver 2 zipped lists
print("This is the Second Version")
new_headers_zip = []
for top_element, bottom_element in zip(top_header, bottom_header):
    selected_header = combine_headers(top_element, bottom_element)
    new_headers_zip.append(selected_header)

print(new_headers_zip)
