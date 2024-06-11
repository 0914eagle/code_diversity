def Strongest_Extension(class_name, extensions):
    
    strongest_extension = extensions[0]
    strength = -1
    for extension in extensions:
        extension_strength = extension.count('A') - extension.count('a')
        if extension_strength > strength:
            strength = extension_strength
            strongest_extension = extension
    return f'{class_name}.{strongest_extension}'


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension