
def get_chapters_to_read(n, pages, k):
    # Find the chapter that Nastya started reading
    current_chapter = 0
    while current_chapter < n and pages[current_chapter][1] < k:
        current_chapter += 1
    
    # Count the number of chapters that haven't been read yet
    chapters_to_read = 0
    for i in range(current_chapter, n):
        if pages[i][0] > k:
            chapters_to_read += 1
    
    return chapters_to_read

def main():
    n = int(input())
    pages = []
    for i in range(n):
        pages.append(list(map(int, input().split())))
    k = int(input())
    print(get_chapters_to_read(n, pages, k))

if __name__ == '__main__':
    main()

