
def is_incomparable(s, w):
    n = len(s)
    for i in range(n):
        if s[i] > w[i] and s[i+1] < w[i+1]:
            return True
    return False

def count_ways(template1, template2):
    n = len(template1)
    ways = 1
    for i in range(n):
        if template1[i] == '?':
            ways *= 10
        if template2[i] == '?':
            ways *= 10
    return ways

def main():
    n = int(input())
    template1 = input()
    template2 = input()
    ways = count_ways(template1, template2)
    print(ways % 1000000007)

if __name__ == '__main__':
    main()

