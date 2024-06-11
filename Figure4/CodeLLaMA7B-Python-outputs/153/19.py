def Strongest_Extension(class_name, extensions):
    
    strongest = 0
    strongest_extension = ''
    for extension in extensions:
        cap = 0
        sm = 0
        for letter in extension:
            if letter.isupper():
                cap += 1
            elif letter.islower():
                sm += 1
        if cap - sm > strongest:
            strongest = cap - sm
            strongest_extension = extension
    return f'{class_name}.{strongest_extension}'


if __name__ == '__main__':
    print