def Strongest_Extension(class_name, extensions):
    
    # your code here
    strongest = 0
    strongest_ext = ''
    for ext in extensions:
        cap = 0
        low = 0
        for letter in ext:
            if letter.isupper():
                cap += 1
            elif letter.islower():
                low += 1
        if cap - low > strongest:
            strongest = cap - low
            strongest_ext = ext
    return class_name + '.' + strongest_ext


if __name__ == '__main__':
    print("Example:")
    print(Strongest