
def get_matches(N, W, H):
    matches = []
    for _ in range(N):
        matches.append(int(input()))
    return matches

def fit_in_box(matches, W, H):
    result = []
    for match in matches:
        if match <= W:
            result.append("DA")
        else:
            result.append("NE")
    return result

def main():
    N, W, H = map(int, input().split())
    matches = get_matches(N, W, H)
    result = fit_in_box(matches, W, H)
    for r in result:
        print(r)

if __name__ == '__main__':
    main()

