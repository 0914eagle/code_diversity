
def f1(p):
    # Initialize the maximum number of elements in the original array
    max_elements = 0
    # Iterate through all possible combinations of two numbers that add up to p
    for i in range(1, int(p/2) + 1):
        for j in range(i, int(p/2) + 1):
            # Check if i and j are distinct and if i + j = p
            if i != j and i + j == p:
                # Calculate the number of elements in the original array
                elements = 1 + i + j
                # Update the maximum number of elements if necessary
                max_elements = max(max_elements, elements)
    return max_elements

def f2(...):
    # Implement f2 according to the problem statement
    ...

if __name__ == '__main__':
    p = int(input())
    print(f1(p))

