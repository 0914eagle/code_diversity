
def f1(s):
    # Calculate the average value of L(C) over all possible sequences C represented by s
    n = len(s)
    count = 0
    sum = 0
    for i in range(1, n+1):
        for j in range(n):
            if s[j] == 'H':
                count += 1
                sum += i
    return sum / count

def f2(s):
    # Calculate the average value of L(C) over all possible sequences C represented by s
    n = len(s)
    count = 0
    sum = 0
    for i in range(1, n+1):
        for j in range(n):
            if s[j] == 'H':
                count += 1
                sum += i
    return sum / count

if __name__ == '__main__':
    s = input()
    print(f1(s))
    print(f2(s))

