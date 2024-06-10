
def get_winners(matches):
    winners = {}
    for match in matches:
        if match[1] == ">":
            winners[match[0]] = match[2]
    return winners

def get_losers(matches):
    losers = {}
    for match in matches:
        if match[1] == ">":
            losers[match[2]] = match[0]
    return losers

def check_consistency(matches):
    winners = get_winners(matches)
    losers = get_losers(matches)
    for match in matches:
        if match[1] == "=":
            if winners[match[0]] != match[2] or losers[match[0]] != match[2]:
                return "inconsistent"
    return "consistent"

if __name__ == '__main__':
    num_players, num_matches = map(int, input().split())
    matches = [tuple(map(int, input().split())) for _ in range(num_matches)]
    print(check_consistency(matches))

