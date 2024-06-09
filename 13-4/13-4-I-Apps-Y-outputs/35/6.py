
def get_input():
    N = int(input())
    S = input()
    return N, S

def get_colors(S):
    colors = set()
    for s in S:
        colors.add(s)
    return colors

def get_number_of_colors(colors):
    if len(colors) == 3:
        return "Three"
    else:
        return "Four"

def main():
    N, S = get_input()
    colors = get_colors(S)
    number_of_colors = get_number_of_colors(colors)
    print(number_of_colors)

if __name__ == '__main__':
    main()

