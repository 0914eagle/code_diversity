
def read_array(n):
    a = list(map(int, input().split()))
    return a

def is_good_array(a):
    if len(a) % 6 != 0:
        return False
    subseq_4 = 0
    subseq_8 = 0
    subseq_15 = 0
    subseq_16 = 0
    subseq_23 = 0
    subseq_42 = 0
    for i in range(len(a)):
        if a[i] == 4:
            subseq_4 += 1
        elif a[i] == 8:
            subseq_8 += 1
        elif a[i] == 15:
            subseq_15 += 1
        elif a[i] == 16:
            subseq_16 += 1
        elif a[i] == 23:
            subseq_23 += 1
        elif a[i] == 42:
            subseq_42 += 1
    if subseq_4 == 0 or subseq_8 == 0 or subseq_15 == 0 or subseq_16 == 0 or subseq_23 == 0 or subseq_42 == 0:
        return False
    return True

def remove_elements(a):
    n = len(a)
    if n == 0:
        return 0
    if is_good_array(a):
        return n
    min_removed = n
    for i in range(n):
        a_copy = a.copy()
        a_copy.pop(i)
        removed = remove_elements(a_copy)
        if removed < min_removed:
            min_removed = removed
    return min_removed

if __name__ == '__main__':
    n = int(input())
    a = read_array(n)
    print(remove_elements(a))

