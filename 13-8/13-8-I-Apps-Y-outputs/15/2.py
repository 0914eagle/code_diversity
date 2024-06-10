
def get_companies(n, k):
    # Implement your solution here
    return r

def get_road_assignment(n, k, r):
    # Implement your solution here
    return c

if __name__ == '__main__':
    n, k = map(int, input().split())
    r = get_companies(n, k)
    c = get_road_assignment(n, k, r)
    print(r)
    print(*c)

