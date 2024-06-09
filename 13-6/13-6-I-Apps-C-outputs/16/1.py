
def is_aesthetic(path_length, colors_used):
    
    for i in range(1, path_length + 1):
        for j in range(i + 1, path_length + 1):
            if (j - i) % path_length > 1 and colors_used >= 2:
                if path_length % (j - i) == 0:
                    return False
    return True


def find_max_colors(path_length):
    
    max_colors = 1
    for i in range(1, path_length + 1):
        if is_aesthetic(path_length, i):
            max_colors = max(max_colors, i)
    return max_colors


if __name__ == '__main__':
    path_length = int(input())
    print(find_max_colors(path_length))

