
def get_colors(n):
    return input().split()

def get_number_of_colors(colors):
    unique_colors = set(colors)
    if len(unique_colors) == 3:
        return "Three"
    else:
        return "Four"

def main():
    n = int(input())
    colors = get_colors(n)
    print(get_number_of_colors(colors))

if __name__ == '__main__':
    main()

