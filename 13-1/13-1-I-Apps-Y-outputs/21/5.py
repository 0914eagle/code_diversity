
def is_square_number(a, b):
    concat = str(a) + str(b)
    sqrt_concat = int(concat) ** 0.5
    return sqrt_concat ** 2 == int(concat)

def main():
    a, b = map(int, input().split())
    if is_square_number(a, b):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

