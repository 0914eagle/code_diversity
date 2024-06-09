
def get_matches(n, w, h):
    matches = []
    for _ in range(n):
        matches.append(int(input()))
    return matches

def fit_matches(matches, w, h):
    return [match for match in matches if match <= w]

def main():
    n, w, h = map(int, input().split())
    matches = get_matches(n, w, h)
    fits = fit_matches(matches, w, h)
    for match in fits:
        print("DA")
    for match in matches:
        if match not in fits:
            print("NE")

if __name__ == '__main__':
    main()

