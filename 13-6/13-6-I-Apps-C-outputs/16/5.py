
def get_path_length(path_length):
    return path_length

def get_number_of_colors(path_length):
    return int(path_length / 2) + 1

def is_aesthetic(path_length, color_1, color_2):
    return (color_1 == color_2) and (path_length % abs(color_1 - color_2) == 0)

def get_maximum_number_of_colors(path_length):
    number_of_colors = get_number_of_colors(path_length)
    for color in range(1, number_of_colors + 1):
        if not is_aesthetic(path_length, color, color):
            return color - 1
    return number_of_colors

if __name__ == '__main__':
    path_length = int(input())
    print(get_maximum_number_of_colors(path_length))

