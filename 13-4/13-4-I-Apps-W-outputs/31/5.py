
def solve(r, b, k):
    # Calculate the maximum number of planks that can be painted with the given coefficients
    max_planks = (r * b) // gcd(r, b)

    # Check if the maximum number of planks is divisible by k
    if max_planks % k == 0:
        return "REBEL"
    else:
        return "OBEY"

def main():
    num_cases = int(input())
    for i in range(num_cases):
        r, b, k = map(int, input().split())
        print(solve(r, b, k))

if __name__ == "__main__":
    main()

