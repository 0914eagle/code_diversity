
def check_package_weight(n, a, b, c, d):
    # Check if the weight of each grain is within the given range
    for i in range(n):
        if a - b <= i <= a + b:
            continue
        else:
            return "No"
    
    # Check if the total weight of all grains is within the given range
    if c - d <= sum(range(n)) <= c + d:
        return "Yes"
    else:
        return "No"

def main():
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, input().split())
        print(check_package_weight(n, a, b, c, d))

if __name__ == '__main__':
    main()

