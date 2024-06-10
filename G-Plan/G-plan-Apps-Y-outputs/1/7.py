
def find_winners(n, p, m, participants):
    scores = {participant: 0 for participant in participants}
    winners = []
    
    for _ in range(m):
        name, points = input().split()
        scores[name] += int(points)
        
        for participant, score in scores.items():
            if score >= p and participant not in winners:
                winners.append(participant)
                if len(winners) == n:
                    break
        
        if len(winners) == n:
            break
    
    if winners:
        for winner in winners:
            print(f"{winner} wins!")
    else:
        print("No winner!")

if __name__ == '__main__':
    n, p, m = map(int, input().split())
    participants = [input() for _ in range(n)]
    find_winners(n, p, m, participants)
