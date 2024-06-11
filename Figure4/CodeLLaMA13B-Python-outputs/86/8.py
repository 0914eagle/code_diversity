def anti_shuffle(s):
    
    return ' '.join([sorted(word) for word in s.split()])


if __name__ == '__main__':
    assert anti_shuffle('Hi') == 'Hi'
    assert anti_shuffle('hello') == 'ehllo'
    assert anti_shuffle('Hello World!!!') == 'Hello !!!Wdlor'
