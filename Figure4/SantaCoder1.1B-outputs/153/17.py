def Strongest_Extension(class_name, extensions):
    
    # Write your code here.
    if len(extensions) == 0:
        return class_name
    else:
        max_strength = 0
        max_extension = ''
        for extension in extensions:
            if len(extension) > len(max_extension):
                max_extension = extension
                max_strength = len(extension) - len(max_extension)
        return class_name + '.' + max_extension[:max_strength]

#