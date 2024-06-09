
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

            # Add the GCD to the set of common divisors
            common_divisors.add(gcd)

    # Return the number of common divisors
    return len(common_divisors)

def find_gcd(a, b):
    # Find the greatest common divisor (GCD) of a and b
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(count_common_divisors(arr))

