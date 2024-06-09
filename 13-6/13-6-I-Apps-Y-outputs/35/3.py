
def get_sand_after_t_seconds(X, t):
    return X - t

def main():
    X, t = map(int, input().split())
    print(get_sand_after_t_seconds(X, t))

if __name__ == '__main__':
    main()

