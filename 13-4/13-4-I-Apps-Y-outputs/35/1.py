
def get_colors(n):
    return [input() for _ in range(n)]

def get_number_of_colors(colors):
    return len(set(colors))

def main():
    n = int(input())
    colors = get_colors(n)
    number_of_colors = get_number_of_colors(colors)
    if number_of_colors == 3:
        print("Three")
    else:
        print("Four")

if __name__ == '__main__':
    main()

