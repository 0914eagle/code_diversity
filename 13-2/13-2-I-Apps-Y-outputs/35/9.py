
def get_number_of_colors(s):
    colors = set(s)
    if len(colors) == 3:
        return "Three"
    else:
        return "Four"

def main():
    n = int(input())
    s = input()
    print(get_number_of_colors(s))

if __name__ == '__main__':
    main()

