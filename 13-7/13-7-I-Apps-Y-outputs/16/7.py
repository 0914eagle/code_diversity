
def get_max_value(operations):
    x = 0
    max_value = 0
    for operation in operations:
        if operation == "I":
            x += 1
        else:
            x -= 1
        max_value = max(max_value, x)
    return max_value

def main():
    n = int(input())
    s = input()
    print(get_max_value(s))

if __name__ == '__main__':
    main()

