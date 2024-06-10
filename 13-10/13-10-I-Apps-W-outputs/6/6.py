
def get_party_from_pair(pair):
    return "A" if pair[0] % 2 == 0 else "B"

def get_party_from_pairs(pairs):
    party = []
    for pair in pairs:
        party.append(get_party_from_pair(pair))
    return party

def main():
    n = int(input())
    pairs = []
    for i in range(5):
        pair_count = int(input())
        pairs.append(input().split())
    party = get_party_from_pairs(pairs)
    print("".join(party))

if __name__ == '__main__':
    main()

