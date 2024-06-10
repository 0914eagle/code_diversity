
def read_input():
    N, M = map(int, input().split())
    matches = []
    for _ in range(M):
        match = input().split()
        matches.append(match)
    return N, M, matches

def find_opponent(player, matches):
    opponent = None
    for match in matches:
        if match[0] == player:
            opponent = match[2]
        elif match[2] == player:
            opponent = match[0]
    return opponent

def check_consistency(N, M, matches):
    for i in range(N):
        opponent = find_opponent(i, matches)
        if opponent is not None:
            if matches[i][1] == "=" and matches[opponent][1] == ">":
                return "inconsistent"
            elif matches[i][1] == ">" and matches[opponent][1] == "=":
                return "inconsistent"
    return "consistent"

def main():
    N, M, matches = read_input()
    print(check_consistency(N, M, matches))

if __name__ == '__main__':
    main()

