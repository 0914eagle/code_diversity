
def get_min_d(a):
    # Calculate the sum of the elements in the array
    sum_a = sum(a)
    # Calculate the minimum and maximum values in the array
    min_a = min(a)
    max_a = max(a)
    # Initialize the minimum D value as -1
    min_d = -1
    # Iterate through all possible D values from 0 to the sum of the elements in the array
    for d in range(sum_a + 1):
        # Calculate the sum of the elements after adding D to some elements and subtracting D from others
        sum_after_d = sum_a + d * (len(a) - min_a) - d * max_a
        # If the sum is equal to the product of the number of elements and the minimum value, we have found the minimum D value
        if sum_after_d == len(a) * min_a:
            min_d = d
            break
    return min_d

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_min_d(a))

if __name__ == '__main__':
    main()

