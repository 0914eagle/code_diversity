
def f(n, a):
    # Initialize a set to store the distinct values of f
    distinct_values = set()
    
    # Iterate over the sequence
    for i in range(n):
        for j in range(i+1, n+1):
            # Calculate the value of f for the current subsequence
            value = gcd(a[i:j])
            
            # Add the value to the set of distinct values
            distinct_values.add(value)
    
    # Return the number of distinct values
    return len(distinct_values)

def gcd(numbers):
    # Calculate the greatest common divisor of a list of numbers
    gcd = 1
    for num in numbers:
        gcd = gcd(gcd, num)
    return gcd

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f(n, a))

