
def input_data():
    X, Y = map(int, input().split())
    return X, Y

def is_valid_combination(X, Y):
    for i in range(1, X+1):
        for j in range(1, Y+1):
            if i + j == X and i * 2 + j * 4 == Y:
                return True
    return False

def main():
    X, Y = input_data()
    if is_valid_combination(X, Y):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

