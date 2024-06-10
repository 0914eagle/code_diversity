
def confusion_sequence(n, c):
    # Calculate the number of ways to form a sequence of length n with c confused pairs
    # We can form a sequence by choosing c pairs of numbers from the n numbers, and then ordering them
    # The number of ways to choose c pairs is n choose c
    # The number of ways to order each pair is 2! = 2
    # Therefore, the total number of ways to form a sequence is (n choose c) * 2^c
    return binomial(n, c) * 2**c

def binomial(n, k):
    # Calculate the binomial coefficient of n and k
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

def count_sequences(n, c):
    # Calculate the number of sequences of length n with c confused pairs
    # We can form a sequence by choosing the first number, then the second number, and so on
    # The number of ways to choose the first number is n
    # The number of ways to choose the second number is n-1
    # And so on
    # Therefore, the total number of ways to form a sequence is n * (n-1) * ... * (n-c+1)
    result = 1
    for i in range(c):
        result *= n - i
    return result

def main():
    n, c = map(int, input().split())
    print(count_sequences(n, c))

if __name__ == '__main__':
    main()

