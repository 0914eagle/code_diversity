
def count_good_phone_numbers(n, k, a, b):
    modulo = 10**9 + 7
    count = 0
    for i in range(10**k):
        number = str(i).zfill(k)
        block = [int(number[j*k:(j+1)*k]) for j in range(n//k)]
        if block[0] != b[0]:
            count += 1
        for i in range(1, n//k):
            if block[i] != b[i] and block[i-1] % a[i] == 0:
                count += 1
    return count % modulo

