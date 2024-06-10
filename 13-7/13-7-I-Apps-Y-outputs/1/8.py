
def get_input():
    return list(map(int, input().split()))

def is_valid_combination(x, y):
    for cranes in range(x+1):
        turtles = x - cranes
        if 2*cranes + 4*turtles == y:
            return True
    return False

def main():
    x, y = get_input()
    if is_valid_combination(x, y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

