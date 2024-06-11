def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = extensions[0]
    for extension in extensions:
        if extension.count('A') - extension.count('a') > strongest.count('A') - strongest.count('a'):
            strongest = extension
    return class_name + '.' + strongest


if __name__ == '__main__':
    print("Example:")
    print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']) == 'Slices.SErviNGSliCes'
    assert Strongest_Extension('Geroge', ['fRieNd', 'Peace', 'loVe']) == 'Geroge.fRieNd'
    assert Strongest_Extension('Stack', ['OvErFlOw', 'CasHEs', 'PEaCe']) == 'Stack.OvErFlOw'
    print("Coding complete? Click 'Check' to earn cool rewards!")
