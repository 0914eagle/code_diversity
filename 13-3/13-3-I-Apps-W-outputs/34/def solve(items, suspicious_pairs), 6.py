
def solve(items, suspicious_pairs):
    # Initialize a dictionary to store the items and their corresponding partners
    partners = {}

    # Iterate over the suspicious pairs and add them to the dictionary
    for pair in suspicious_pairs:
        partners[pair[0]] = pair[1]
        partners[pair[1]] = pair[0]

    # Initialize two lists to store the items for Walter and Jesse
    walter_items = []
    jesse_items = []

    # Iterate over the items and check if they have a partner
    for item in items:
        # If the item has a partner, add it to the list of items for the person who does not have it
        if item in partners:
            if partners[item] in walter_items:
                jesse_items.append(item)
            else:
                walter_items.append(item)
        # If the item does not have a partner, add it to the list of items for Walter
        else:
            walter_items.append(item)

    # Return the lists of items for Walter and Jesse
    return walter_items, jesse_items

