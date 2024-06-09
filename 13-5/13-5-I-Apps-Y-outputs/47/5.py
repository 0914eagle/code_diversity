
def get_matches_that_fit_in_box(matches, box_width, box_height):
    return [match for match in matches if match <= box_width]

def get_matches_that_do_not_fit_in_box(matches, box_width, box_height):
    return [match for match in matches if match > box_width]

def main():
    num_matches, box_width, box_height = map(int, input().split())
    matches = [int(input()) for _ in range(num_matches)]
    matches_that_fit = get_matches_that_fit_in_box(matches, box_width, box_height)
    matches_that_do_not_fit = get_matches_that_do_not_fit_in_box(matches, box_width, box_height)
    for match in matches_that_fit:
        print("DA")
    for match in matches_that_do_not_fit:
        print("NE")

if __name__ == '__main__':
    main()

