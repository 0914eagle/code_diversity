
def f1(a, b, x):
    # Initialize variables
    n = a + b
    s = ""
    count_zeros = 0
    count_ones = 0
    indices = []

    # Construct the string
    for i in range(n):
        if count_zeros < a and count_ones < b:
            s += "0"
            count_zeros += 1
        elif count_zeros == a and count_ones < b:
            s += "1"
            count_ones += 1
        else:
            s += "0"
            count_zeros += 1
            indices.append(i)

    # Shuffle the string
    import random
    random.shuffle(indices)
    for i in indices:
        s = s[:i] + "1" + s[i + 1:]

    # Return the string
    return s

def f2(a, b, x):
    # Initialize variables
    n = a + b
    s = ""
    count_zeros = 0
    count_ones = 0
    indices = []

    # Construct the string
    for i in range(n):
        if count_zeros < a and count_ones < b:
            s += "0"
            count_zeros += 1
        elif count_zeros == a and count_ones < b:
            s += "1"
            count_ones += 1
        else:
            s += "0"
            count_zeros += 1
            indices.append(i)

    # Shuffle the string
    import random
    random.shuffle(indices)
    for i in indices:
        s = s[:i] + "1" + s[i + 1:]

    # Return the string
    return s

if __name__ == '__main__':
    a, b, x = map(int, input().split())
    print(f1(a, b, x))
    print(f2(a, b, x))

