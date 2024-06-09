
def get_input():
    n, m = map(int, input().split())
    assignments = list(map(int, input().split()))
    return n, m, assignments

def solve(n, m, assignments):
    days_spent = 0
    for assignment in assignments:
        days_spent += assignment
        if days_spent > n:
            return -1
    return n - days_spent

def main():
    n, m, assignments = get_input()
    print(solve(n, m, assignments))

if __name__ == '__main__':
    main()

