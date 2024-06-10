
def find_winners(n, p, m, participants):
    scores = {}
    winners = []
    
    for participant in participants:
        name, points = participant.split()
        points = int(points)
        
        if name not in scores:
            scores[name] = 0
        
        scores[name] += points
        
        if scores[name] >= p and name not in winners:
            winners.append(name)
            if len(winners) == n:
                break
    
    if not winners:
        print("No winner!")
    else:
        for winner in winners:
            print(f"{winner} wins!")

if __name__ == '__main__':
    n, p, m = map(int, input().split())
    participants = [input() for _ in range(n)] + [input() for _ in range(m)]
    find_winners(n, p, m, participants)
