
def get_chapters(pages, k):
    chapters = []
    start = 1
    for page in pages:
        if page < k:
            chapters.append(start)
        else:
            start = page + 1
    return chapters

def get_number_of_chapters(n, pages, k):
    chapters = get_chapters(pages, k)
    return n - len(chapters)

if __name__ == '__main__':
    n = int(input())
    pages = []
    for i in range(n):
        l, r = map(int, input().split())
        pages.extend(range(l, r+1))
    k = int(input())
    print(get_number_of_chapters(n, pages, k))

