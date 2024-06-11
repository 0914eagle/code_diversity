def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest_extension = extensions[0]
    strongest_extension_strength = 0
    for extension in extensions:
        strength = sum(1 for char in extension if char.isupper()) - sum(1 for char in extension if char.islower())
        if strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = strength
    return class_name + '.' + strongest_extension


if __name__ == '__main__':
