
def f1(a, b, x):
    # Initialize variables
    n = a + b
    s = []
    zeroes = 0
    ones = 0
    indices = []
    
    # Add zeroes to the string
    while zeroes < a:
        s.append("0")
        zeroes += 1
    
    # Add ones to the string
    while ones < b:
        s.append("1")
        ones += 1
    
    # Add indices to the list
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            indices.append(i)
    
    # Check if there are enough indices
    if len(indices) < x:
        return -1
    
    # Shuffle the indices
    import random
    random.shuffle(indices)
    
    # Flip the bits at the selected indices
    for i in indices[:x]:
        if s[i] == "0":
            s[i] = "1"
        else:
            s[i] = "0"
    
    return "".join(s)

def f2(...):
    ...

if __name__ == '__main__':
    a, b, x = map(int, input().split())
    s = f1(a, b, x)
    print(s)

