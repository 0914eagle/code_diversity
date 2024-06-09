
def solve(n, m, roads):
    # Initialize the minimum cost to decorate the city as -1
    min_cost = -1
    
    # Create a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    # Iterate through all possible combinations of decorations
    for decoration1 in range(3):
        for decoration2 in range(3):
            if (decoration1 + decoration2) % 3 != 1:
                continue
            for decoration3 in range(3):
                if (decoration1 + decoration3) % 3 != 1:
                    continue
                for decoration4 in range(3):
                    if (decoration2 + decoration4) % 3 != 1:
                        continue
                    for decoration5 in range(3):
                        if (decoration3 + decoration5) % 3 != 1:
                            continue
                        for decoration6 in range(3):
                            if (decoration4 + decoration6) % 3 != 1:
                                continue
                            for decoration7 in range(3):
                                if (decoration5 + decoration7) % 3 != 1:
                                    continue
                                for decoration8 in range(3):
                                    if (decoration6 + decoration8) % 3 != 1:
                                        continue
                                    for decoration9 in range(3):
                                        if (decoration7 + decoration9) % 3 != 1:
                                            continue
                                        for decoration10 in range(3):
                                            if (decoration8 + decoration10) % 3 != 1:
                                                continue
                                            total_cost = decoration1 + decoration2 + decoration3 + decoration4 + decoration5 + decoration6 + decoration7 + decoration8 + decoration9 + decoration10
                                            if total_cost % 2 == 1:
                                                min_cost = min(min_cost, total_cost)
    
    # Return the minimum cost
    return min_cost

