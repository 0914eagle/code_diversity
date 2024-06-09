
def f1(A, B, S):
    count = 0
    smallest = 0
    for i in range(A, B+1):
        if sum(int(j) for j in str(i)) == S:
            count += 1
            if count == 1:
                smallest = i
    return count, smallest

def f2(...):
    ...

if __name__ == '__main__':
    A, B, S = map(int, input().split())
    count, smallest = f1(A, B, S)
    print(count)
    print(smallest)

