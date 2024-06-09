
def special_numbers(n, k):
    count = 0
    for i in range(1, n+1):
        binary = bin(i)[2:]
        ones = binary.count('1')
        if ones == k:
            count += 1
    return count % (10**9 + 7)
