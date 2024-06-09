
def sand_in_upper_bulb(X, t):
    return X - (t * 1)

def sand_in_lower_bulb(X, t):
    return t * 1

if __name__ == '__main__':
    X, t = map(int, input().split())
    print(sand_in_upper_bulb(X, t))

