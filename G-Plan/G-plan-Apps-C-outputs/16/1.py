
def count_sequences(n):
    MOD = 10**9 + 7
    result = 1
    for i in range(1, n):
        result = (result * (i + 1)) % MOD
    return (n * result) % MOD

if __name__ == "__main__":
    n = int(input())
    print(count_sequences(n))
