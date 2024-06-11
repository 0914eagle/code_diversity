def Strongest_Extension(class_name, extensions):
    
    strongest_extension = ''
    strongest_extension_strength = 0
    for extension in extensions:
        extension_strength = extension.count('A') - extension.count('a')
        if extension_strength > strongest_extension_strength:
            strongest_extension_strength = extension_strength
            strongest_extension = extension
    return f'{class_name}.{strongest_extension}'


if __name__ == '__main__