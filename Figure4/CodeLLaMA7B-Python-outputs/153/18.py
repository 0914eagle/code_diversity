def Strongest_Extension(class_name, extensions):
    
    strongest = extensions[0]
    strength = -1
    for extension in extensions:
        cap = 0
        sm = 0
        for letter in extension:
            if letter.isupper():
                cap += 1
            elif letter.islower():
                sm += 1
        if cap - sm > strength:
            strength = cap - sm
            strongest = extension
    return f"{class_name}.{strongest}"


if __name__ == '__main__':
    print("Example:")
   