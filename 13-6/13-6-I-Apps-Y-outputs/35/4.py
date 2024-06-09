
def get_sand_amount(x, t):
    return x - (t * 1)

def main():
    x, t = map(int, input().split())
    print(get_sand_amount(x, t))

if __name__ == '__main__':
    main()

