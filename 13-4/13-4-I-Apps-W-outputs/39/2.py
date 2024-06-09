
def f1(l, d, n):
    # Calculate the available space for the additional birds
    available_space = l - (n * d) - (2 * 6)
    return available_space // d

def f2(l, d, n):
    # Calculate the maximum number of additional birds that can sit on the wire
    max_additional_birds = (l - (n * d) - (2 * 6)) // d
    return max_additional_birds

if __name__ == '__main__':
    l, d, n = map(int, input().split())
    print(f2(l, d, n))

