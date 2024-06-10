
def find_winners(n, p, m, participants):
    scores = {}
    winners = []
    
    for i in range(n):
        scores[participants[i]] = 0
    
    for _ in range(m):
        name, points = input().split()
        scores[name] += int(points)
        
        if scores[name] >= p and name not in winners:
            winners.append(name)
            print(f"{name} wins!")
    
    if not winners:
        print("No winner!")

if __name__ == "__main__":
    n, p, m = map(int, input().split())
    participants = [input() for _ in range(n)]
    
    find_winners(n, p, m, participants)
