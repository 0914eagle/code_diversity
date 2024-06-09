
def sand_in_upper_bulb(X, t):
    return X - t

def main():
    X, t = map(int, input().split())
    print(sand_in_upper_bulb(X, t))

if __name__ == '__main__':
    main()

