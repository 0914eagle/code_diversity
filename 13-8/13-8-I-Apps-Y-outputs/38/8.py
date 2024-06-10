
def get_substring_count(string, substring):
    count = 0
    for i in range(len(string)):
        if string[i:i+len(substring)] == substring:
            count += 1
    return count

def get_min_string(t, k):
    n = len(t)
    for i in range(1, n+1):
        s = t*i
        if get_substring_count(s, t) == k:
            return s
    return ""

def main():
    n, k = map(int, input().split())
    t = input()
    print(get_min_string(t, k))

if __name__ == '__main__':
    main()

