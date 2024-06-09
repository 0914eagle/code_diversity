
def get_input():
    N, W, H = map(int, input().split())
    matches = [int(input()) for _ in range(N)]
    return N, W, H, matches

def fit_in_box(match, box_width, box_height):
    return match <= box_width and match <= box_height

def main():
    N, W, H, matches = get_input()
    for match in matches:
        if fit_in_box(match, W, H):
            print("DA")
        else:
            print("NE")

if __name__ == '__main__':
    main()

