
def get_matches_that_fit(matches, box_dimensions):
    w, h = box_dimensions
    return [match for match in matches if match <= w]

def get_matches_that_do_not_fit(matches, box_dimensions):
    w, h = box_dimensions
    return [match for match in matches if match > w]

def main():
    num_matches, box_width, box_height = map(int, input().split())
    matches = [int(input()) for _ in range(num_matches)]
    fits = get_matches_that_fit(matches, (box_width, box_height))
    does_not_fit = get_matches_that_do_not_fit(matches, (box_width, box_height))
    for match in fits:
        print("DA")
    for match in does_not_fit:
        print("NE")

if __name__ == '__main__':
    main()

