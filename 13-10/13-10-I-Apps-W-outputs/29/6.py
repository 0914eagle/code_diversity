
def check_package(n, a, b, c, d):
    # Check if the range of weights for each grain is valid
    if b < a or d < c:
        return "No"
    
    # Check if the total weight of the package is within the given range
    if c - d > n * (a + b) or c + d < n * (a - b):
        return "No"
    
    # Check if the weights of all grains are integers and within the given range
    for i in range(n):
        if (a - b) % i != 0 or (a + b) % i != 0:
            return "No"
    
    return "Yes"

def main():
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = map(int, input().split())
        print(check_package(n, a, b, c, d))

if __name__ == '__main__':
    main()

