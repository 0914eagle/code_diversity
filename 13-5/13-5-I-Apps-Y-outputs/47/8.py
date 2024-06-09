
def get_matches_that_fit(box_width, box_height, matches):
    matches_that_fit = []
    for match in matches:
        if match <= box_width:
            matches_that_fit.append(match)
    return matches_that_fit

def get_matches_that_do_not_fit(box_width, box_height, matches):
    matches_that_do_not_fit = []
    for match in matches:
        if match > box_width:
            matches_that_do_not_fit.append(match)
    return matches_that_do_not_fit

def main():
    box_width, box_height, num_matches = map(int, input().split())
    matches = []
    for _ in range(num_matches):
        matches.append(int(input()))
    matches_that_fit = get_matches_that_fit(box_width, box_height, matches)
    matches_that_do_not_fit = get_matches_that_do_not_fit(box_width, box_height, matches)
    for match in matches_that_fit:
        print("DA")
    for match in matches_that_do_not_fit:
        print("NE")

if __name__ == '__main__':
    main()

