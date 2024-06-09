
def is_m_perfect(x, y, m):
    return x >= m or y >= m

def get_min_operations(x, y, m):
    if is_m_perfect(x, y, m):
        return 0
    if x < 0 and y < 0:
        return -1
    if x < 0:
        return get_min_operations(-x, y, m)
    if y < 0:
        return get_min_operations(x, -y, m)
    return get_min_operations(x+y, y, m) + 1

if __name__ == '__main__':
    x, y, m = map(int, input().split())
    print(get_min_operations(x, y, m))

