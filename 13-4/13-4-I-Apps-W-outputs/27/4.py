
def f1(n, m):
    # Calculate the number of subsequences for each sequence of length n
    # and return the sum modulo 10^9 + 7
    return sum(f2(n, m)) % 1000000007

def f2(n, m):
    # Initialize a list to store the number of subsequences for each sequence
    num_subseq = [0] * (n + 1)
    num_subseq[0] = 1

    # Iterate over the elements of the sequence
    for i in range(n):
        # Calculate the number of subsequences for the current element
        # by adding the number of subsequences of the previous element
        # and the number of subsequences of the previous element with the current element
        num_subseq[i + 1] = (num_subseq[i] * m) % 1000000007
        num_subseq[i + 1] = (num_subseq[i + 1] + num_subseq[i]) % 1000000007

    return num_subseq

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

