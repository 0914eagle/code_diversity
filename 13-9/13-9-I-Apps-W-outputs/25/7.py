
def is_incomparable(s, w):
    n = len(s)
    for i in range(n):
        if s[i] > w[i] and s[i+1] < w[i+1]:
            return True
    return False

def count_ways(s, w):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == '?':
            for j in range(10):
                s_new = s[:i] + str(j) + s[i+1:]
                if is_incomparable(s_new, w):
                    count += 1
        elif w[i] == '?':
            for j in range(10):
                w_new = w[:i] + str(j) + w[i+1:]
                if is_incomparable(s, w_new):
                    count += 1
    return count

def main():
    n = int(input())
    s = input()
    w = input()
    print(count_ways(s, w) % 1000000007)

if __name__ == '__main__':
    main()

