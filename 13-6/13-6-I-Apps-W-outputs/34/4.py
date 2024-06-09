
def get_antipalindromic_permutation(s):
    n = len(s)
    if n % 2 == 1:
        return ""
    s_list = list(s)
    for i in range(n // 2):
        s_list[i], s_list[n - i - 1] = s_list[n - i - 1], s_list[i]
    return "".join(s_list)

def get_max_beauty(s, b):
    n = len(s)
    if n % 2 == 1:
        return 0
    s_list = list(s)
    b_list = list(b)
    for i in range(n // 2):
        s_list[i], s_list[n - i - 1] = s_list[n - i - 1], s_list[i]
        b_list[i], b_list[n - i - 1] = b_list[n - i - 1], b_list[i]
    return sum(b_list)

if __name__ == '__main__':
    n = int(input())
    s = input()
    b = input()
    b = list(map(int, b.split()))
    print(get_max_beauty(s, b))

