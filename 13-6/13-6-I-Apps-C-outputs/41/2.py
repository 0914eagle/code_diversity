
def get_total_width_of_lawns(n, s, g):
    total_width = 0
    for i in range(n):
        total_width += g[i]
    return total_width

def get_new_widths_of_road(n, s, g):
    new_widths = []
    for i in range(n):
        new_widths.append(s[i] + g[i])
    return new_widths

def main():
    n = int(input())
    s = list(map(int, input().split()))
    g = list(map(int, input().split()))
    total_width = get_total_width_of_lawns(n, s, g)
    new_widths = get_new_widths_of_road(n, s, g)
    print(total_width)
    print(" ".join(map(str, new_widths)))

if __name__ == '__main__':
    main()

