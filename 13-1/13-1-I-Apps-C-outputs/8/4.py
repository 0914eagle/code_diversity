
def get_min_operations(x, y, m):
    if x >= m and y >= m:
        return 0
    if x < 0 and y < 0:
        return -1
    if x < 0:
        return get_min_operations(-x, y, m)
    if y < 0:
        return get_min_operations(x, -y, m)
    return 1 + get_min_operations(x+y, y, m)

def main():
    x, y, m = map(int, input().split())
    print(get_min_operations(x, y, m))

if __name__ == '__main__':
    main()

