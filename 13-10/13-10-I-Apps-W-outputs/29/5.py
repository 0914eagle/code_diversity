
def check_package(n, a, b, c, d):
    # Check if a and b are valid
    if a - b < 0 or a + b > c + d:
        return "No"
    
    # Check if the total weight of the package is within the given range
    if c - d > n * (a + b) or c + d < n * (a - b):
        return "No"
    
    # Check if each grain weighs an integer number of grams
    for i in range(n):
        if (a - b) % 2 == 1:
            return "No"
    
    return "Yes"

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        n, a, b, c, d = map(int, input().split())
        print(check_package(n, a, b, c, d))

if __name__ == '__main__':
    main()

