
def calculate(A, B, C):
    if C == "+":
        return A + B
    elif C == "-":
        return A - B
    elif C == "*":
        return A * B
    else:
        return A / B

def main():
    A = float(input())
    B = float(input())
    C = input()
    print(calculate(A, B, C))

if __name__ == '__main__':
    main()

