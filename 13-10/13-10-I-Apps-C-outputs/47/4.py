
def read_input():
    N, M = map(int, input().split())
    matches = []
    for _ in range(M):
        match = input().split()
        matches.append((int(match[0]), match[1], int(match[2])))
    return N, M, matches

def check_consistency(matches):
    players = [[] for _ in range(N)]
    for match in matches:
        players[match[0]].append(match[2])
        players[match[2]].append(match[0])
    
    for i in range(N):
        for j in range(i+1, N):
            if len(players[i]) != len(players[j]):
                return "inconsistent"
    
    return "consistent"

def main():
    N, M, matches = read_input()
    print(check_consistency(matches))

if __name__ == '__main__':
    main()

