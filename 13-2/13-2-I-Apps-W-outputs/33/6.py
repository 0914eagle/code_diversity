
def solve(layout1, layout2, text):
    # Create a dictionary to map the keys of the first layout to the keys of the second layout
    key_map = {layout1[i]: layout2[i] for i in range(len(layout1))}
    
    # Create a new string with the mapped keys
    mapped_text = ''
    for char in text:
        if char in key_map:
            mapped_text += key_map[char]
        else:
            mapped_text += char
    
    return mapped_text

