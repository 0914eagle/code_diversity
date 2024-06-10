
def get_input():
    return [int(x) for x in input().split()]

def solve(X, Y):
    for cranes in range(X+1):
        turtles = X - cranes
        if 2*cranes + 4*turtles == Y:
            return "Yes"
    return "No"

def main():
    X, Y = get_input()
    print(solve(X, Y))

if __name__ == '__main__':
    main()

