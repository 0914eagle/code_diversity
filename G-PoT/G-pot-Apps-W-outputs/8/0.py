
def count_2_3_integers(l, r):
    count = 0
    for i in range(l, r+1):
        num = i
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        if num == 1:
            count += 1
    return count

l, r = map(int, input().split())
result = count_2_3_integers(l, r)
print(result)
