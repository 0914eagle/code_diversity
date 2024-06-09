
def get_matches(N, W, H):
    matches = []
    for _ in range(N):
        matches.append(int(input()))
    return matches

def fit_in_box(match, W, H):
    if match <= W:
        return "DA"
    else:
        return "NE"

def main():
    N, W, H = map(int, input().split())
    matches = get_matches(N, W, H)
    for match in matches:
        print(fit_in_box(match, W, H))

if __name__ == '__main__':
    main()

