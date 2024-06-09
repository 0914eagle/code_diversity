
def solve(a):
    # Step 1: Initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    
    # Step 2: Iterate through the array and delete elements based on the parity of the previous element
    for i in range(len(a)):
        if i % 2 == 0:
            # If the previous element is even, delete the next odd element
            if a[i] % 2 == 0 and i < len(a) - 1 and a[i + 1] % 2 == 1:
                sum_non_deleted -= a[i + 1]
                a = a[:i + 1] + a[i + 2:]
        else:
            # If the previous element is odd, delete the next even element
            if a[i] % 2 == 1 and i < len(a) - 1 and a[i + 1] % 2 == 0:
                sum_non_deleted -= a[i + 1]
                a = a[:i + 1] + a[i + 2:]
    
    # Step 3: Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

