
def get_ice_cream(n, k, a, b, t, u):
    # Initialize the maximum tastiness and cost
    max_tastiness = 0
    max_cost = 0
    
    # Loop through each possible combination of scoops
    for num_scoops in range(1, n + 1):
        for scoop_order in itertools.permutations(range(k), num_scoops):
            # Calculate the tastiness and cost of this combination
            tastiness = 0
            cost = 0
            for i in range(num_scoops):
                tastiness += t[scoop_order[i]]
                cost += a
            for i in range(num_scoops - 1):
                tastiness += u[scoop_order[i]][scoop_order[i + 1]]
                cost += b
            
            # Update the maximum tastiness and cost if necessary
            if tastiness > max_tastiness or (tastiness == max_tastiness and cost < max_cost):
                max_tastiness = tastiness
                max_cost = cost
    
    # Return the maximum possible tastiness per gold coin ratio
    if max_cost == 0:
        return 0
    else:
        return max_tastiness / max_cost

def main():
    n, k, a, b = map(int, input().split())
    t = list(map(int, input().split()))
    u = []
    for i in range(k):
        u.append(list(map(int, input().split())))
    print(get_ice_cream(n, k, a, b, t, u))

if __name__ == '__main__':
    main()

