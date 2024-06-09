
def f1(s):
    # Calculate the average value of L(C) over all possible sequences C represented by s
    n = len(s)
    count = 0
    total = 0
    for i in range(1, n+1):
        for j in range(n-i+1):
            sub_s = s[j:j+i]
            count += 1
            total += f2(sub_s)
    return total / count

def f2(s):
    # Calculate the number of operations before Prof. Tuy stops for the given initial configuration s
    n = len(s)
    if s.count("H") == n:
        return 0
    if s.count("H") == 0:
        return n
    for i in range(1, n):
        if s[:i].count("H") == i:
            return i + f2(s[i:])
    return n

if __name__ == '__main__':
    s = input()
    print(f1(s))

