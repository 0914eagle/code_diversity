
def incomparable(s, w):
    n = len(s)
    for i in range(n):
        if s[i] > w[i] and s[i-1] < w[i-1]:
            return True
    return False

def count_ways(s, w):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == "?":
            count += n - i
        elif w[i] == "?":
            count += i + 1
    return count

def main():
    n = int(input())
    s = input()
    w = input()
    if "?" not in s and "?" not in w:
        print(1)
    else:
        if incomparable(s, w):
            print(0)
        else:
            print(count_ways(s, w) % 1000000007)

if __name__ == '__main__':
    main()

