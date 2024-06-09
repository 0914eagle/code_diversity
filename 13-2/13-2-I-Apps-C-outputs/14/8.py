
def f1(string, explosion):
    while explosion in string:
        index = string.index(explosion)
        string = string[:index] + string[index+len(explosion):]
    return string

def f2(string, explosion):
    while True:
        new_string = ""
        for i in range(len(string)):
            if string[i:i+len(explosion)] == explosion:
                continue
            new_string += string[i]
        if new_string == string:
            break
        string = new_string
    return string

if __name__ == '__main__':
    string, explosion = input(), input()
    print(f2(string, explosion))

