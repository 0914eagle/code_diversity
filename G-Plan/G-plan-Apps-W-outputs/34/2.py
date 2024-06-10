
MOD = 10**9 + 7

def is_good_number(number, a, b, k):
    for i in range(len(a)):
        block = number[i*k : (i+1)*k]
        block_int = int(''.join(block))
        if block[0] == str(b[i]) or block_int % a[i] != 0:
            return False
    return True

def count_good_numbers(n, k, a, b):
    count = 0
    for num in range(10**(n-k)):
        number = str(num).zfill(n-k)
        if is_good_number(number, a, b, k):
            count += 1
    return count % MOD

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = count_good_numbers(n, k, a, b)
    print(result)
