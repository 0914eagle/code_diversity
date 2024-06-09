
def get_input():
    return int(input())

def solve(n):
    count = 0
    for a in range(1, n+1):
        for b in range(1, n+1):
            c = n - a*b
            if a*b + c == n and a > 0 and b > 0 and c > 0:
                count += 1
    return count

def main():
    n = get_input()
    print(solve(n))

if __name__ == '__main__':
    main()

