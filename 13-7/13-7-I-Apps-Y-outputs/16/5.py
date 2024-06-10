
def get_max_value(s):
    x = 0
    for i in s:
        if i == "I":
            x += 1
        else:
            x -= 1
    return x

def main():
    n = int(input())
    s = input()
    print(get_max_value(s))

if __name__ == '__main__':
    main()

