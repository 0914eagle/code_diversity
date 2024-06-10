
def get_chapters_to_read(pages, k):
    # Find the chapter that Nastya finished reading
    finished_chapter = 0
    for i in range(len(pages)):
        if k <= pages[i][1]:
            finished_chapter = i
            break
    
    # Count the number of chapters that haven't been read
    chapters_to_read = 0
    for i in range(finished_chapter+1, len(pages)):
        chapters_to_read += 1
    
    return chapters_to_read

def main():
    n = int(input())
    pages = []
    for i in range(n):
        l, r = map(int, input().split())
        pages.append([l, r])
    k = int(input())
    print(get_chapters_to_read(pages, k))

if __name__ == '__main__':
    main()

