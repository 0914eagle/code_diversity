
def can_reach_n(n, m, d, c):
    # Your code here
    pass

def move_platforms(n, m, c):
    # Your code here
    pass

if __name__ == '__main__':
    n, m, d = map(int, input().split())
    c = list(map(int, input().split()))
    print(can_reach_n(n, m, d, c))
    print(move_platforms(n, m, c))

