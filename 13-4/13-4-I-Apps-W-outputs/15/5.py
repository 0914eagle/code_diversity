
def get_different_string(s1, s2, t):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            break
    else:
        return -1
    s3 = list(s1)
    s3[i] = 'a' if s1[i] == 'b' else 'b'
    if f(s1, s3) == t and f(s2, s3) == t:
        return ''.join(s3)
    return -1

def f(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

if __name__ == '__main__':
    n, t = map(int, input().split())
    s1 = input()
    s2 = input()
    print(get_different_string(s1, s2, t))

