
def get_unread_chapters(chapters, k):
    unread_chapters = 0
    for chapter in chapters:
        if chapter[0] > k:
            unread_chapters += 1
        elif chapter[1] < k:
            pass
        else:
            unread_chapters += 1
    return unread_chapters

def main():
    n = int(input())
    chapters = []
    for i in range(n):
        l, r = map(int, input().split())
        chapters.append([l, r])
    k = int(input())
    print(get_unread_chapters(chapters, k))

if __name__ == '__main__':
    main()

