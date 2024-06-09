
def get_return_day(n, p):
    # Initialize a dictionary to store the return day for each kid
    return_day = {}
    for i in range(n):
        return_day[i+1] = 0
    
    # Iterate through the permutation and update the return day for each kid
    for i in range(n):
        kid = p[i]
        if kid != i+1:
            return_day[kid] += 1
    
    # Return the return day for each kid
    return [return_day[i+1] for i in range(n)]

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(*get_return_day(n, p))

if __name__ == '__main__':
    main()

