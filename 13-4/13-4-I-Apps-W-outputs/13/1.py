
def solve(f, b):
    # Initialize a dictionary to store the replacements
    replacements = {}

    # Loop through the replacements and add them to the dictionary
    for i in range(len(f)):
        replacements[f[i]] = b[i]

    # Initialize a set to store the unique elements of the original sequence
    unique_elements = set()

    # Loop through the replacements and check if the original element is unique
    for element in replacements.keys():
        if element not in unique_elements:
            unique_elements.add(element)
        else:
            return "Ambiguity"

    # Check if there is exactly one unique element in the original sequence
    if len(unique_elements) == 1:
        # If there is exactly one unique element, return the corresponding replacement
        return "Possible", list(replacements.values())
    else:
        # If there is no unique element, return "Impossible"
        return "Impossible"

