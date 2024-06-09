
def apaxian_name_extender(name, parent):
    # Check if the name ends with e
    if name.endswith("e"):
        return name + "x" + parent
    
    # Check if the name ends with a vowel (a, i, o, or u)
    if name[-1] in "aiou":
        return name[:-1] + "ex" + parent
    
    # Check if the name already ends with "ex"
    if name.endswith("ex"):
        return name + parent
    
    # If none of the above conditions are met, return the extended name
    return name + "ex" + parent

