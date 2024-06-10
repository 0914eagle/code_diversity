
def is_valid_package(n, a, b, c, d):
    # Check if a and b are valid
    if a < b:
        return "No"
    
    # Check if c and d are valid
    if c < d:
        return "No"
    
    # Check if the total weight of the package is between c - d and c + d
    if c - d <= n * (a - b) <= c + d:
        return "Yes"
    
    return "No"

def main():
    num_cases = int(input())
    for _ in range(num_cases):
        n, a, b, c, d = map(int, input().split())
        print(is_valid_package(n, a, b, c, d))

if __name__ == '__main__':
    main()

