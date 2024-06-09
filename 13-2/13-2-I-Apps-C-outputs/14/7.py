
def f1(string, explosion):
    while explosion in string:
        string = string.replace(explosion, "")
    return string

def f2(string, explosion):
    while True:
        if explosion in string:
            string = string.replace(explosion, "")
        else:
            break
    return string

if __name__ == '__main__':
    string, explosion = input(), input()
    print(f1(string, explosion))
    print(f2(string, explosion))

