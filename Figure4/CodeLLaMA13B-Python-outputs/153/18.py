def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = 0
    strongest_ext = ''
    for ext in extensions:
        cap = 0
        sm = 0
        for char in ext:
            if char.isupper():
                cap += 1
            elif char.islower():
                sm += 1
        if cap - sm > strongest:
            strongest = cap - sm
            strongest_ext = ext
    return class_name + '.' + strongest_ext


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('Geroge', ['fRieNd', 'pEaCe', 'Chocolate']) == 'Geroge.fRieNd'
    assert Strongest_Extension('Stack', ['oFwEeK', 'PLaCE', 'Chocolate']) == 'Stack.oFwEeK'
    print("Coding complete? Click 'Check' to earn cool rewards!")
