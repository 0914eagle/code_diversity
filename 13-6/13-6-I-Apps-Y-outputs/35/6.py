
def get_sand_in_upper_bulb(x, t):
    return x - t

def get_sand_in_lower_bulb(x, t):
    return t

if __name__ == '__main__':
    x, t = map(int, input().split())
    print(get_sand_in_upper_bulb(x, t))

