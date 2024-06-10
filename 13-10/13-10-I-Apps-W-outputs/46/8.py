
def get_unread_chapters(n, chapters, k):
    unread_chapters = 0
    for i in range(n):
        if chapters[i][0] > k:
            unread_chapters += 1
        elif chapters[i][1] < k:
            unread_chapters += 1
    return unread_chapters

def main():
    n = int(input())
    chapters = []
    for i in range(n):
        chapters.append(list(map(int, input().split())))
    k = int(input())
    print(get_unread_chapters(n, chapters, k))

if __name__ == '__main__':
    main()

