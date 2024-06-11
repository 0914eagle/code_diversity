def Strongest_Extension(class_name, extensions):
    
    strongest_extension = extensions[0]
    strongest_strength = -1
    for extension in extensions:
        strength = extension.count('A') - extension.count('a')
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_extension = extension
    return class_name + '.' + strongest_extension


if __name__ == '__main__':
    print("Example:")
    print(Strongest_