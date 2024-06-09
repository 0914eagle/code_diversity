
def f1(s):
    # Calculate the average value of L(C) over all possible sequences C represented by s
    n = len(s)
    count = 0
    total = 0
    for i in range(1, n+1):
        for j in range(n-i+1):
            sub_s = s[j:j+i]
            if sub_s.count("H") == i:
                count += 1
                total += i
    return total / count

def f2(s):
    # Calculate the average value of L(C) over all possible sequences C represented by s
    n = len(s)
    count = 0
    total = 0
    for i in range(1, n+1):
        for j in range(n-i+1):
            sub_s = s[j:j+i]
            if sub_s.count("H") == i:
                count += 1
                total += i
    return total / count

if __name__ == '__main__':
    s = input()
    print(f1(s))

