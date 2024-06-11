def Strongest_Extension(class_name, extensions):
    
    strongest = 0
    strongest_ext = ''
    for ext in extensions:
        cap = 0
        sm = 0
        for c in ext:
            if c.isupper():
                cap += 1
            elif c.islower():
                sm += 1
        if cap - sm > strongest:
            strongest = cap - sm
            strongest_ext = ext
    return f'{class_name}.{strongest_ext}'


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CC']) == 'my_class.AA'
    assert Strongest_Extension('my_class', ['AAA', 'Be', 'CCC']) == 'my_class.AAA'
    assert Strongest_Extension('my_class', ['BA', 'Be', 'CC']) == 'my_class.BA'
    assert Strongest_Extension('my_class', ['AA', 'foo', 'CC']) == 'my_class.foo'
    assert Strongest_Extension('my_class', ['AA', 'Ba', 'CC']) == 'my_class.Ba'
    assert Strongest_Extension('my_class', ['AA', 'Be', 'CCC']) == 'my_class.CCC'
    assert Strongest_Extension('my_class', ['AA', 'Ba', 'CCC']) == 'my_class.CCC'
    assert Strongest_Extension('my_class', ['AA', 'Ba', 'CC']) == 'my_class.CC'
    print("Coding complete? Click 'Check' to earn cool rewards!")