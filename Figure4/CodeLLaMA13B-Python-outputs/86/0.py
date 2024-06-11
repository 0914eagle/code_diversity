def anti_shuffle(s):
    
    return ' '.join([sorted(word) for word in s.split()])


if __name__ == '__main__':
    print(anti_shuffle('Hello World!!!'))
