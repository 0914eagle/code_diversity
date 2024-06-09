
def get_box_dimensions():
    return map(int, input().split())

def get_match_lengths():
    return [int(input()) for _ in range(int(input()))]

def fits_in_box(match_length, box_width, box_height):
    return match_length <= box_width and match_length <= box_height

def main():
    box_width, box_height = get_box_dimensions()
    match_lengths = get_match_lengths()
    for match_length in match_lengths:
        if fits_in_box(match_length, box_width, box_height):
            print("DA")
        else:
            print("NE")

if __name__ == '__main__':
    main()

