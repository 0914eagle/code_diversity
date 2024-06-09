
def get_colors(n):
    return input().split()

def get_number_of_colors(colors):
    colors_set = set(colors)
    if len(colors_set) == 3:
        return "Three"
    elif len(colors_set) == 4:
        return "Four"
    else:
        return "Error"

def main():
    n = int(input())
    colors = get_colors(n)
    print(get_number_of_colors(colors))

if __name__ == '__main__':
    main()

