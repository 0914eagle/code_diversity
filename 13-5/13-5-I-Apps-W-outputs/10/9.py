
def modular_equation(a, b):
    if a == 0 and b == 0:
        return "infinity"
    elif a == 0 and b != 0:
        return 0
    else:
        solutions = 0
        for i in range(1, b+1):
            if a % i == b:
                solutions += 1
        return solutions

def main():
    a, b = map(int, input().split())
    print(modular_equation(a, b))

if __name__ == '__main__':
    main()

