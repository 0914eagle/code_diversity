
def f1(a, b, x):
    # Initialize variables
    n = a + b
    s = ""
    count_zeroes = 0
    count_ones = 0
    count_indices = 0
    
    # Construct the string
    while count_indices < x:
        if count_zeroes < a:
            s += "0"
            count_zeroes += 1
        elif count_ones < b:
            s += "1"
            count_ones += 1
        else:
            break
        count_indices += 1
    
    # Add remaining characters
    while len(s) < n:
        if count_zeroes < a:
            s += "0"
            count_zeroes += 1
        elif count_ones < b:
            s += "1"
            count_ones += 1
        else:
            break
    
    return s

def f2(s):
    # Find the indices where s[i] != s[i + 1]
    indices = []
    for i in range(len(s) - 1):
        if s[i] != s[i + 1]:
            indices.append(i)
    
    return indices

if __name__ == '__main__':
    a, b, x = map(int, input().split())
    s = f1(a, b, x)
    indices = f2(s)
    print(s)
    print(indices)

