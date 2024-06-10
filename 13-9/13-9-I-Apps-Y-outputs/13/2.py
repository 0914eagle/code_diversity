
def is_good(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] + a[j] in (2**k for k in range(32)):
                return True
    return False

def remove_elements(a):
    while len(a) > 0 and not is_good(a):
        a.pop()
    return len(a)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(remove_elements(a))

