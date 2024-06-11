def Strongest_Extension(class_name, extensions):
    
    strongest_extension = extensions[0]
    strongest_strength = -1
    for extension in extensions:
        extension_strength = extension.count('A') - extension.count('a')
        if extension_strength > strongest_strength:
            strongest_strength = extension_strength
            strongest_extension = extension
    return class_name + '.' + strongest_extension


if __name__ == '__main__':
    print("Example: