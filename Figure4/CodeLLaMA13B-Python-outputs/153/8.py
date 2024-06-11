def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = 0
    strongest_extension = ''
    for extension in extensions:
        cap = 0
        sm = 0
        for letter in extension:
            if letter.isupper():
                cap += 1
            else:
                sm += 1
        if cap - sm > strongest:
            strongest = cap - sm
            strongest_extension = extension
    return class_name + '.' + strongest_extension


if