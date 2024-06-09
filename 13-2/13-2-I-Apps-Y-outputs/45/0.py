
def count_common_divisors(arr):
    # Initialize a set to store the common divisors
    common_divisors = set()

    # Iterate through the array
    for i in range(len(arr)):
        # Get the current number
        num = arr[i]

        # Iterate through the previous numbers
        for j in range(i):
            # Get the previous number
            prev_num = arr[j]

            # Find the greatest common divisor (GCD) of the current number and the previous number
            gcd = find_gcd(num, prev_num)

            # If the GCD is 1, it means the current number and the previous number are coprime,
            # so we can add the current number to the set of common divisors
            if gcd == 1:
                common_divisors.add(num)
                break

    # Return the length of the set of common divisors
    return len(common_divisors)

def find_gcd(a, b):
    # Base case: if b is 0, the GCD is a
    if b == 0:
        return a

    # Recursive case: find the GCD of b and the remainder of a divided by b
    return find_gcd(b, a % b)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_common_divisors(arr))

