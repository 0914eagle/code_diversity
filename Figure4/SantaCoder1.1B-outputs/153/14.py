def Strongest_Extension(class_name, extensions):
    
    if len(extensions) == 0:
        return class_name
    else:
        strongest_extension = extensions[0]
        for extension in extensions:
            if extension.isupper() and strongest_extension.islower():
                strongest_extension = extension
            elif extension.islower() and strongest_extension.isupper():
                strongest_extension = extension
        return class_name + '.' + strongest_extension

