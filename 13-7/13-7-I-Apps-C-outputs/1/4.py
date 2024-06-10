
def assign_toys(n_kids, n_toys, playtime, events):
    # Initialize a dictionary to store the toys played with by each kid
    toys_played_with = {}
    for event in events:
        kid, toy = event[1], event[2]
        if kid not in toys_played_with:
            toys_played_with[kid] = []
        toys_played_with[kid].append(toy)

    # Initialize a dictionary to store the number of times each toy was played with
    toys_played_count = {}
    for kid, toys in toys_played_with.items():
        for toy in toys:
            if toy not in toys_played_count:
                toys_played_count[toy] = 0
            toys_played_count[toy] += 1

    # Sort the toys by the number of times they were played with, in descending order
    sorted_toys = sorted(toys_played_count.items(), key=lambda x: x[1], reverse=True)

    # Create a list to store the final assignment of toys to kids
    assigned_toys = []

    # Loop through the kids and assign them toys based on their envy and inflexibility
    for kid in range(1, n_kids + 1):
        # Find the toy that the kid envies the most
        envied_toy = None
        for toy, count in sorted_toys:
            if toy not in toys_played_with[kid]:
                envied_toy = toy
                break

        # If the kid has no envied toy, assign them their current toy
        if envied_toy is None:
            assigned_toys.append(toys_played_with[kid][0])
        # If the kid has an envied toy, assign them that toy
        else:
            assigned_toys.append(envied_toy)

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

