
def get_matches_that_fit(matches, box_width, box_height):
    matches_that_fit = []
    for match in matches:
        if match <= box_width:
            matches_that_fit.append(match)
    return matches_that_fit

def get_matches_that_do_not_fit(matches, box_width, box_height):
    matches_that_do_not_fit = []
    for match in matches:
        if match > box_width:
            matches_that_do_not_fit.append(match)
    return matches_that_do_not_fit

def main():
    num_matches, box_width, box_height = map(int, input().split())
    matches = []
    for _ in range(num_matches):
        matches.append(int(input()))
    matches_that_fit = get_matches_that_fit(matches, box_width, box_height)
    matches_that_do_not_fit = get_matches_that_do_not_fit(matches, box_width, box_height)
    for match in matches_that_fit:
        print("DA")
    for match in matches_that_do_not_fit:
        print("NE")

if __name__ == '__main__':
    main()

