def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = 0
    strongest_extension = ''
    for extension in extensions:
        cap = 0
        sm = 0
        for letter in extension:
            if letter.isupper():
                cap += 1
            elif letter.islower():
                sm += 1
        if cap - sm > strongest:
            strongest = cap - sm
            strongest_extension = extension
    return class_name + '.' + strongest_extension


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('Geroge', ['fRieNd', 'Peace', 'loVe']) == 'Geroge.fRieNd'
    assert Strongest_Extension('Smiles', ['laugh', 'Smile', 'grin']) == 'Smiles.Smile'
    print("Coding complete? Click 'Check' to earn cool rewards!")
