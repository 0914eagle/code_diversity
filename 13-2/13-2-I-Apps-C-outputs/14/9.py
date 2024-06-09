
def f1(string, explosion):
    while explosion in string:
        index = string.index(explosion)
        string = string[:index] + string[index+len(explosion):]
    return string

def f2(string, explosion):
    if string == "":
        return "FRULA"
    else:
        return string

if __name__ == '__main__':
    string, explosion = input().split()
    result = f1(string, explosion)
    print(f2(result, explosion))

