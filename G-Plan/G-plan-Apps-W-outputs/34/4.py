
MOD = 10**9 + 7

def is_good_number(num, a, b, k):
    num_str = str(num).zfill(k)
    for i in range(k):
        block = int(num_str[i*k:(i+1)*k])
        if block % a[i] != 0 or int(num_str[i*k]) == b[i]:
            return False
    return True

def count_good_numbers(n, k, a, b):
    count = 0
    for num in range(10**n):
        if is_good_number(num, a, b, k):
            count += 1
    return count % MOD

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = count_good_numbers(n, k, a, b)
    print(result)
