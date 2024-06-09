
def get_min_d(a):
    # Calculate the difference between the maximum and minimum values in the array
    diff = max(a) - min(a)
    
    # If the difference is zero, return zero
    if diff == 0:
        return 0
    
    # Initialize the minimum non-negative integer value of D
    d = 0
    
    # Iterate through the array
    for i in range(len(a)):
        # If the current value is not equal to the minimum value, add the minimum non-negative integer value of D to it
        if a[i] != min(a):
            a[i] += d
        
        # If the current value is not equal to the maximum value, subtract the minimum non-negative integer value of D from it
        if a[i] != max(a):
            a[i] -= d
    
    # Check if all values in the array are equal
    if all(x == a[0] for x in a):
        # If they are equal, return the minimum non-negative integer value of D
        return d
    else:
        # If they are not equal, return -1
        return -1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_d(a))

if __name__ == '__main__':
    main()

