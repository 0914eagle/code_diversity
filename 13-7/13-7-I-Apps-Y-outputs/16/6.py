
def get_max_value(string):
    x = 0
    max_value = 0
    for char in string:
        if char == "I":
            x += 1
            max_value = max(max_value, x)
        else:
            x -= 1
            max_value = max(max_value, x)
    return max_value

def main():
    n = int(input())
    string = input()
    print(get_max_value(string))

if __name__ == '__main__':
    main()

