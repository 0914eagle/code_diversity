
def is_good(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if i != j and a[i] + a[j] in [2**d for d in range(31)]:
                return True
    return False

def find_min_to_remove(a):
    min_to_remove = len(a)
    for i in range(len(a)):
        temp = a[:i] + a[i+1:]
        if is_good(temp):
            min_to_remove = min(min_to_remove, len(a) - len(temp))
    return min_to_remove

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(find_min_to_remove(a))

