def Strongest_Extension(class_name, extensions):
    
    # your code here
    # your code here
    class_name = class_name.lower()
    strength = 0
    strongest_extension = ''
    for extension in extensions:
        extension = extension.lower()
        if (extension.count('a') - extension.count('b') > strength):
            strength = extension.count('a') - extension.count('b')
            strongest_extension = extension
    return class_name + '.' + strongest_extension

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

