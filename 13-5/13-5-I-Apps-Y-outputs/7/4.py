
def f1(X, Y, Z):
    return (X - Z) // (Y + Z)

def f2(X, Y, Z):
    return (X - Y) // Y

if __name__ == '__main__':
    X, Y, Z = map(int, input().split())
    print(f1(X, Y, Z))

