
def get_chapter_count(chapters, k):
    count = 0
    for chapter in chapters:
        if chapter[0] <= k <= chapter[1]:
            count += 1
        elif chapter[0] > k:
            break
    return count

def get_chapters(n, l_list, r_list):
    chapters = []
    for i in range(n):
        chapters.append([l_list[i], r_list[i]])
    return chapters

if __name__ == '__main__':
    n = int(input())
    l_list = []
    r_list = []
    for i in range(n):
        l, r = map(int, input().split())
        l_list.append(l)
        r_list.append(r)
    k = int(input())
    chapters = get_chapters(n, l_list, r_list)
    count = get_chapter_count(chapters, k)
    print(count)

