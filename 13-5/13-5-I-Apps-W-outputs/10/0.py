
def modular_equation(a, b):
    if a == 0 and b == 0:
        return "infinity"
    else:
        solutions = 0
        for x in range(1, b+1):
            if a % x == b:
                solutions += 1
        return solutions

def main():
    a, b = map(int, input().split())
    print(modular_equation(a, b))

if __name__ == '__main__':
    main()

