
def check_package(n, a, b, c, d):
    # Check if the weight of each grain is within the given range
    for i in range(n):
        if not (a-b <= i <= a+b):
            return "No"
    
    # Check if the total weight of the package is within the given range
    if not (c-d <= sum(range(n)) <= c+d):
        return "No"
    
    return "Yes"

def main():
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, input().split())
        print(check_package(n, a, b, c, d))

if __name__ == '__main__':
    main()

