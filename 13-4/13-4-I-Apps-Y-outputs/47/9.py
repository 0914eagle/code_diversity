
def f1(n, s):
    # Calculate the number of regular bracket sequences of length 2n
    # containing the given bracket sequence s as a substring
    count = 0
    for i in range(2**n):
        sequence = bin(i)[2:].zfill(n)
        if s in sequence:
            count += 1
    return count

def f2(n, s):
    # Calculate the number of regular bracket sequences of length 2n
    # containing the given bracket sequence s as a substring
    # and return the result modulo 10^9+7
    count = f1(n, s)
    return count % 1000000007

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(f2(n, s))

