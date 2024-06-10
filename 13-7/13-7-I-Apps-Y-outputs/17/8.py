
def find_return_days(n, p):
    # Initialize a list to store the return days for each kid
    return_days = [0] * n
    # Iterate through each day
    for day in range(1, n + 1):
        # Iterate through each kid
        for kid in range(n):
            # If the kid's book is returned to him, set his return day to the current day
            if p[kid] == kid:
                return_days[kid] = day
    return return_days

def main():
    queries = int(input())
    for _ in range(queries):
        n = int(input())
        p = list(map(int, input().split()))
        return_days = find_return_days(n, p)
        print(*return_days)

if __name__ == '__main__':
    main()

