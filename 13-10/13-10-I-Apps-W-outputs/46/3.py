
def get_number_of_chapters_to_read(chapters, marked_page):
    num_chapters_read = 0
    for chapter in chapters:
        if marked_page <= chapter[1]:
            break
        num_chapters_read += 1
    return len(chapters) - num_chapters_read

def get_chapters(n):
    chapters = []
    for i in range(n):
        l, r = map(int, input().split())
        chapters.append([l, r])
    return chapters

def get_marked_page(chapters):
    marked_page = int(input())
    return marked_page

if __name__ == '__main__':
    n = int(input())
    chapters = get_chapters(n)
    marked_page = get_marked_page(chapters)
    print(get_number_of_chapters_to_read(chapters, marked_page))

