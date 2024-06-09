
def is_aesthetic(path_length, color_count):
    # Check if the path is aesthetic with the given color count
    for i in range(1, path_length + 1):
        for j in range(i + 1, path_length + 1):
            if path_length % abs(i - j) == 0 and color_count > 1:
                return True
    return False


def find_max_color_count(path_length):
    # Find the maximum number of colors that can be used to make the path aesthetic
    max_color_count = 1
    for i in range(2, path_length + 1):
        if is_aesthetic(path_length, i):
            max_color_count = i
    return max_color_count


if __name__ == '__main__':
    path_length = int(input())
    print(find_max_color_count(path_length))

