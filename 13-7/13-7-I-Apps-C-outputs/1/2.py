
def assign_toys(n_kids, n_toys, playtime, events):
    # Initialize a dictionary to store the toys played with by each kid
    toys_played = {}
    for event in events:
        kid, toy = event[1], event[2]
        if kid not in toys_played:
            toys_played[kid] = []
        if toy != 0:
            toys_played[kid].append(toy)
    
    # Initialize a dictionary to store the number of times each toy was played with
    toy_count = {}
    for kid, toys in toys_played.items():
        for toy in toys:
            if toy not in toy_count:
                toy_count[toy] = 0
            toy_count[toy] += 1
    
    # Sort the toys by the number of times they were played with, in descending order
    sorted_toys = sorted(toy_count.items(), key=lambda x: x[1], reverse=True)
    
    # Assign the toys to the kids in order of their envy rating
    assigned_toys = []
    for i in range(n_kids):
        assigned_toys.append(sorted_toys[i][0])
    
    return assigned_toys

def main():
    n_kids, n_toys = map(int, input().split())
    playtime, n_events = map(int, input().split())
    events = []
    for _ in range(n_events):
        events.append(list(map(int, input().split())))
    assigned_toys = assign_toys(n_kids, n_toys, playtime, events)
    print(*assigned_toys)

if __name__ == '__main__':
    main()

