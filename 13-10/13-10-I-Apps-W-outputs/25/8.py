
def solve_query(start, end):
    # Implement your solution here
    return start

def main():
    n, m, c_l, c_e, v = map(int, input().split())
    stairs = set(map(int, input().split()))
    elevators = set(map(int, input().split()))
    q = int(input())
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        start = (x1, y1)
        end = (x2, y2)
        print(solve_query(start, end))

if __name__ == '__main__':
    main()

