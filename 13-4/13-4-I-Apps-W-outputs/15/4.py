
def get_different_strings(s1, s2, t):
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            s3 = s1[:i] + "a" + s1[i+1:]
            if f(s1, s3) == t and f(s2, s3) == t:
                return s3
    return -1

def f(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count

if __name__ == '__main__':
    n, t = map(int, input().split())
    s1 = input()
    s2 = input()
    print(get_different_strings(s1, s2, t))

