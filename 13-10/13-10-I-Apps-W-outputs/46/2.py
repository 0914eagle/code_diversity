
def get_unread_chapters(n, l, r, k):
    unread_chapters = 0
    for i in range(n):
        if l[i] > k:
            unread_chapters += 1
        elif r[i] < k:
            unread_chapters += 1
    return unread_chapters

def main():
    n = int(input())
    l = []
    r = []
    k = 0
    for i in range(n):
        l_i, r_i = map(int, input().split())
        l.append(l_i)
        r.append(r_i)
    k = int(input())
    unread_chapters = get_unread_chapters(n, l, r, k)
    print(unread_chapters)

if __name__ == '__main__':
    main()

