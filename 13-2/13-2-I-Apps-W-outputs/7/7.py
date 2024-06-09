
def f1(n, a):
    # Initialize variables
    odd_count = 0
    subsegments = []
    
    # Iterate through the sequence
    for i in range(n):
        # Check if the current element is odd
        if a[i] % 2 == 1:
            # If it is, increment the odd count
            odd_count += 1
        
        # If the current element is the first element of a subsegment
        if i % 2 == 0:
            # Add the current element to the subsegment
            subsegments.append(a[i])
        
        # If the current element is the last element of a subsegment
        if i % 2 == 1:
            # Add the current element to the subsegment
            subsegments[-1].append(a[i])
    
    # Check if the number of odd elements is odd
    if odd_count % 2 == 1:
        return "Yes"
    else:
        return "No"

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

