
def get_max_prettiness(a):
    # Sort the array in descending order
    a.sort(reverse=True)
    # Initialize the maximum prettiness as 0
    max_prettiness = 0
    # Loop through the array
    for i in range(len(a)):
        # Check if the current element is divisible by the next element
        if a[i] % a[i+1] == 0:
            # If it is, add it to the maximum prettiness
            max_prettiness += a[i]
        # If the current element is not divisible by the next element, break the loop
        else:
            break
    # Return the maximum prettiness
    return max_prettiness

def get_max_prettiness_three(a):
    # Sort the array in descending order
    a.sort(reverse=True)
    # Initialize the maximum prettiness as 0
    max_prettiness = 0
    # Loop through the array
    for i in range(len(a)):
        # Check if the current element is divisible by the next two elements
        if a[i] % a[i+1] == 0 and a[i] % a[i+2] == 0:
            # If it is, add it to the maximum prettiness
            max_prettiness += a[i]
        # If the current element is not divisible by the next two elements, break the loop
        else:
            break
    # Return the maximum prettiness
    return max_prettiness

def get_max_prettiness_two(a):
    # Sort the array in descending order
    a.sort(reverse=True)
    # Initialize the maximum prettiness as 0
    max_prettiness = 0
    # Loop through the array
    for i in range(len(a)):
        # Check if the current element is divisible by the next element
        if a[i] % a[i+1] == 0:
            # If it is, add it to the maximum prettiness
            max_prettiness += a[i]
        # If the current element is not divisible by the next element, break the loop
        else:
            break
    # Return the maximum prettiness
    return max_prettiness

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        if n == 1:
            print(get_max_prettiness(a))
        elif n == 2:
            print(get_max_prettiness_two(a))
        elif n == 3:
            print(get_max_prettiness_three(a))
        else:
            print("Invalid input")

