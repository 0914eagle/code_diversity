
def f1(p):
    # Initialize the maximum number of elements in the original array
    max_elements = 0
    # Iterate through all possible combinations of two numbers
    for i in range(1, p + 1):
        for j in range(i + 1, p + 1):
            # Check if the concatenation of i and j is less than or equal to p
            if str(i) + str(j) <= str(p):
                # Increment the maximum number of elements in the original array
                max_elements += 1
    return max_elements

def f2(...):
    # Implement f2 according to the problem statement
    ...

if __name__ == '__main__':
    p = int(input())
    print(f1(p))

