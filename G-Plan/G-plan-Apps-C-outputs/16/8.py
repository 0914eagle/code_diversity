
def count_sequences(n):
    MOD = 10**9 + 7
    result = 1
    for i in range(1, n):
        result = (result * (n + i)) % MOD
    return result

if __name__ == '__main__':
    n = int(input())
    print(count_sequences(n))
