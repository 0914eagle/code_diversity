
def find_min_m(s):
    a = [s]
    i = 1
    while True:
        if a[i] in a[:i]:
            return i
        if a[i] % 2 == 0:
            a.append(a[i] // 2)
        else:
            a.append(3 * a[i] + 1)
        i += 1

s = int(input())
print(find_min_m(s))

