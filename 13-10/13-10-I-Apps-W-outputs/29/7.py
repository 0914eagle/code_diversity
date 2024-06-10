
def check_consistency(n, a, b, c, d):
    # Check if a and b are valid
    if a < 0 or b < 0 or a - b < 0:
        return "No"
    
    # Check if c and d are valid
    if c < 0 or d < 0 or c - d < 0:
        return "No"
    
    # Check if the total weight of the package is within the given range
    if c - d > n * (a + b) or c + d < n * (a - b):
        return "No"
    
    return "Yes"

def main():
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, input().split())
        print(check_consistency(n, a, b, c, d))

if __name__ == '__main__':
    main()

