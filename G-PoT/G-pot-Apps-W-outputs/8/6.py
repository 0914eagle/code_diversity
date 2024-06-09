
def count_2_3_integers(l, r):
    def is_2_3_integer(num):
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        return num == 1

    count = 0
    for i in range(l, r+1):
        if is_2_3_integer(i):
            count += 1
    return count

l, r = map(int, input().split())
print(count_2_3_integers(l, r))
