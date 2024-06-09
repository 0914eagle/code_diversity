
def solve(first_layout, second_layout, text):
    # Create a dictionary to map the first layout to the second layout
    layout_map = {}
    for i in range(len(first_layout)):
        layout_map[first_layout[i]] = second_layout[i]

    # Create a new string with the mapped characters
    mapped_text = ""
    for char in text:
        if char in layout_map:
            mapped_text += layout_map[char]
        else:
            mapped_text += char

    return mapped_text

