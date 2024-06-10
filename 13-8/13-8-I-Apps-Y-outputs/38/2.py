
def find_substring(t, k):
    n = len(t)
    s = ""
    for i in range(k):
        s += t
    return s

def main():
    n, k = map(int, input().split())
    t = input()
    print(find_substring(t, k))

if __name__ == '__main__':
    main()

