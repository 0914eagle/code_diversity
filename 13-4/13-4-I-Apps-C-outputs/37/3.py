
def get_input():
    n = int(input())
    pairs = []
    for i in range(n):
        a, b = map(int, input().split())
        pairs.append((a, b))
    return n, pairs

def get_valid_equation(pair):
    a, b = pair
    if a + b != 0:
        return str(a) + " + " + str(b) + " = " + str(a + b)
    elif a - b != 0:
        return str(a) + " - " + str(b) + " = " + str(a - b)
    elif a * b != 0:
        return str(a) + " * " + str(b) + " = " + str(a * b)
    else:
        return "impossible"

def main():
    n, pairs = get_input()
    for pair in pairs:
        print(get_valid_equation(pair))

if __name__ == '__main__':
    main()

