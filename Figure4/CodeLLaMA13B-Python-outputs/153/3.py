def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = extensions[0]
    strongest_strength = 0
    for extension in extensions:
        strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        if strength > strongest_strength:
            strongest = extension
            strongest_strength = strength
    return class_name + '.' + strongest


if __name__ == '__main__':
    print("Example