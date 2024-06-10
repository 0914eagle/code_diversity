
def get_input():
    return [int(x) for x in input().split()]

def get_equation(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                if i != j and i != k and j != k:
                    for op in ["+", "-", "*", "/"]:
                        if eval(str(numbers[i]) + op + str(numbers[j])) == numbers[k]:
                            return str(numbers[i]) + op + str(numbers[j]) + "=" + str(numbers[k])
    return "No solution"

def main():
    numbers = get_input()
    print(get_equation(numbers))

if __name__ == '__main__':
    main()

