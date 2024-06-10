
def get_possible_suspects(n, p, coders):
    possible_suspects = set()
    for coder in coders:
        for suspect in coder:
            if len(possible_suspects) < p:
                possible_suspects.add(suspect)
            elif suspect in possible_suspects:
                return len(possible_suspects)
    return len(possible_suspects)

def get_number_of_possible_two_suspect_sets(n, p, coders):
    possible_suspects = set()
    for coder in coders:
        for suspect in coder:
            if len(possible_suspects) < p:
                possible_suspects.add(suspect)
            elif suspect in possible_suspects:
                return len(possible_suspects)
    return len(possible_suspects)

def main():
    n, p = map(int, input().split())
    coders = []
    for _ in range(n):
        coder = set(map(int, input().split()))
        coders.append(coder)
    print(get_number_of_possible_two_suspect_sets(n, p, coders))

if __name__ == '__main__':
    main()

