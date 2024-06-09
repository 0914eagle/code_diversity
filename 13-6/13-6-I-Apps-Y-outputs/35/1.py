
def get_sand_in_upper_bulb(X, t):
    return X - t

def get_sand_in_lower_bulb(X, t):
    return t

if __name__ == '__main__':
    X, t = map(int, input().split())
    print(get_sand_in_upper_bulb(X, t))

