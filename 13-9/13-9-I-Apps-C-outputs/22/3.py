
def get_string(a_00, a_01, a_10, a_11):
    # Initialize variables
    s = ""
    i = 0
    j = 0
    k = 0
    l = 0

    # Calculate the number of zeros and ones in the string
    n_zeros = a_00 + a_01
    n_ones = a_10 + a_11

    # Check if the number of zeros and ones is valid
    if n_zeros + n_ones > 1000000:
        return "Impossible"

    # Build the string
    while i < n_zeros and j < n_ones:
        if i < a_00:
            s += "0"
            i += 1
        elif j < a_10:
            s += "1"
            j += 1
        elif i < a_01:
            s += "0"
            i += 1
        else:
            s += "1"
            j += 1

    # Add trailing zeros if necessary
    while i < n_zeros:
        s += "0"
        i += 1

    # Add trailing ones if necessary
    while j < n_ones:
        s += "1"
        j += 1

    return s

def main():
    a_00, a_01, a_10, a_11 = map(int, input().split())
    print(get_string(a_00, a_01, a_10, a_11))

if __name__ == '__main__':
    main()

