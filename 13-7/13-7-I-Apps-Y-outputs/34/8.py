
def is_sorted(p):
    return sorted(p) == p

def swap_elements(p, i, j):
    p[i], p[j] = p[j], p[i]
    return p

def can_sort_in_ascending_order(p):
    if len(p) == 1:
        return True
    if len(p) == 2:
        return p[0] < p[1]
    if p[0] < p[1] and can_sort_in_ascending_order(p[1:])[0]:
        return True
    if p[0] > p[1] and can_sort_in_ascending_order(swap_elements(p, 0, 1))[0]:
        return True
    return False

if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().split()))
    print("YES") if can_sort_in_ascending_order(p) else print("NO")

