
def f1(k):
    count = 0
    for i in range(1, k+1, 2):
        for j in range(2, k+1, 2):
            count += 1
    return count

def f2(k):
    count = 0
    for i in range(2, k+1, 2):
        for j in range(1, k+1, 2):
            count += 1
    return count

if __name__ == '__main__':
    k = int(input())
    print(f1(k) + f2(k))

