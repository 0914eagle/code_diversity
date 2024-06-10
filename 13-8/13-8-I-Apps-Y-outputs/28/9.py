
def get_equation(a, b, c):
    for operation in ["+", "-", "*", "/"]:
        for x in range(1, 100):
            if eval(str(a) + operation + str(x)) == c:
                return str(a) + operation + str(x) + "=" + str(c)
    return "No solution"

def main():
    a, b, c = map(int, input("Enter three integers: ").split())
    print(get_equation(a, b, c))

if __name__ == '__main__':
    main()

