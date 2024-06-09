
def get_min_moves(a, b):
    if a == b:
        return 0
    if a > b:
        return get_min_moves(a-1, b) + 1
    else:
        return get_min_moves(a+1, b) + 1

def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(get_min_moves(a, b))

if __name__ == '__main__':
    main()

