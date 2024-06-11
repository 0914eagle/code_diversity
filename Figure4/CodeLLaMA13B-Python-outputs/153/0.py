def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = extensions[0]
    strongest_strength = 0
    for extension in extensions:
        strength = 0
        for letter in extension:
            if letter.isupper():
                strength += 1
            elif letter.islower():
                strength -= 1
        if strength > strongest_strength:
            strongest = extension
            strongest_strength = strength
    return class_name + '.' + strongest


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['abA', 'Be', 'CC']) == 'my_class.Be'
    assert Strongest_Extension('my_class', ['abA', 'cC']) == 'my_class.abA'
    assert Strongest_Extension('my_class', ['4A', 'cC']) == 'my_class.4A'
    assert Strongest_Extension('my_class', ['4A', 'cCc']) == 'my_class.cCc'
    assert Strongest_Extension('my_class', ['4A', 'cCc', '']) == 'my_class.4A'
    assert Strongest_Extension('my_class', ['4A', 'cCc', 'd']) == 'my_class.cCc'
    assert Strongest_Extension('my_class', ['4A', 'cCc', 'd', '']) == 'my_class.cCc'
    print("Coding complete? Click 'Check' to earn cool rewards!")
