
def name_directory(names):
    # sort the names by age in ascending order
    names.sort(key=lambda x: x[2])
    # create a dictionary to map sex to title
    title_map = {"M": "Mr.", "F": "Ms."}
    # iterate through the names and print them in the desired format
    for name in names:
        print(f"{title_map[name[3]]} {name[0]} {name[1]}")
    return names

