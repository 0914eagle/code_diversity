
def get_max_divisible(A, K):
    # Initialize the maximum divisible value as 1
    max_divisible = 1
    # Loop through each element in A
    for i in range(len(A)):
        # Find the greatest common divisor (GCD) of the current element and the maximum divisible value
        gcd = gcd_of_two(A[i], max_divisible)
        # Update the maximum divisible value using the GCD and the current element
        max_divisible = lcm_of_two(gcd, A[i])
    # Return the maximum divisible value
    return max_divisible

def gcd_of_two(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm_of_two(a, b):
    return a * b // gcd_of_two(a, b)

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    print(get_max_divisible(A, K))

if __name__ == "__main__":
    main()

