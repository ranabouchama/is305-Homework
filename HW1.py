# =====================================================================
# IS305: Homework 1 (Updated Fall 2024)
# Header Merger Script
# =====================================================================

# 1. Paste in the variables with the row data
top_header = ['', '', 'Name', '', 'National Pokédex\nnumber', 'Type(s)', '', 'Evolves from', 'Evolves into', 'Notes']
bottom_header = ['','Generation', 'English', 'Japanese', '', 'Primary', 'Secondary', '', '', '']

# 2. Assert that the two lists are the same length
assert len(top_header) == len(bottom_header), "Error: Header lists must be of the same length."

# 3. Define the combine_headers function
def combine_headers(top_str, bottom_str):
    """
    Takes in two strings and uses merging rules to select the appropriate header value.
    """
    # Assert that they are both strings
    assert isinstance(top_str, str), "Error: top_str must be a string string type."
    assert isinstance(bottom_str, str), "Error: bottom_str must be a string string type."
    
    # Selection Rules applied using a single if-elif-else block
    if bottom_str != "" and top_str != "":
        # Prioritize the bottom row's content when both have content
        selection = bottom_str
    elif bottom_str != "" and top_str == "":
        # Prioritize content over empty values (bottom has content)
        selection = bottom_str
    elif top_str != "" and bottom_str == "":
        # Prioritize content over empty values (top has content)
        selection = top_str
    else:
        # Use "MissingLabel" if both are empty
        selection = "MissingLabel"
        
    # One and only one return statement returning the selection variable
    return selection


# =====================================================================
# VERSION 1: Mutual Index Loop Lookup
# =====================================================================
print("--- Running Version 1: Mutual Index ---")
new_headers_index = []

# Loop over the two lists using index values
for index in range(len(top_header)):
    # Lookup the elements using the mutual index
    selected_header = combine_headers(top_header[index], bottom_header[index])
    # Collect up the selected headers using a list accumulator pattern
    new_headers_index.append(selected_header)

print(new_headers_index)


# =====================================================================
# VERSION 2: Zipped Lists Loop
# =====================================================================
print("\n--- Running Version 2: Zipped Lists ---")
new_headers_zip = []

# Zip the lists together before comparison
for top_element, bottom_element in zip(top_header, bottom_header):
    # Send the pair of strings directly to the function
    selected_header = combine_headers(top_element, bottom_element)
    # Collect up the selected headers using a list accumulator pattern
    new_headers_zip.append(selected_header)

print(new_headers_zip)
