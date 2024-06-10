
def get_chapters_to_read(n, chapters, k):
    chapters_to_read = 0
    for i in range(n):
        if chapters[i][0] > k:
            chapters_to_read += 1
    return chapters_to_read

def get_chapter_indices(chapters):
    chapter_indices = []
    for i in range(len(chapters)):
        chapter_indices.append(chapters[i][0])
    return chapter_indices

def get_chapter_lengths(chapters):
    chapter_lengths = []
    for i in range(len(chapters)):
        chapter_lengths.append(chapters[i][1] - chapters[i][0] + 1)
    return chapter_lengths

def main():
    n = int(input())
    chapters = []
    for i in range(n):
        chapter = list(map(int, input().split()))
        chapters.append(chapter)
    k = int(input())
    chapter_indices = get_chapter_indices(chapters)
    chapter_lengths = get_chapter_lengths(chapters)
    chapters_to_read = get_chapters_to_read(n, chapters, k)
    print(chapters_to_read)

if __name__ == '__main__':
    main()

