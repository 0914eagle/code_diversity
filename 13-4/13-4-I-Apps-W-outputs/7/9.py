
def f1(n, m, similar_pairs):
    # Initialize the number of ways to split problems as 0
    num_ways = 0
    
    # Loop through each pair of similar problems
    for u, v in similar_pairs:
        # If problem u is used in division 1 and problem v is used in division 2, increment the number of ways
        if u in division_1 and v in division_2:
            num_ways += 1
    
    # Return the number of ways to split problems
    return num_ways

def f2(n, m, similar_pairs):
    # Initialize the number of ways to split problems as 0
    num_ways = 0
    
    # Loop through each pair of similar problems
    for u, v in similar_pairs:
        # If problem u is used in division 1 and problem v is used in division 2, increment the number of ways
        if u in division_1 and v in division_2:
            num_ways += 1
    
    # Return the number of ways to split problems
    return num_ways

if __name__ == '__main__':
    n, m = map(int, input().split())
    similar_pairs = []
    for _ in range(m):
        u, v = map(int, input().split())
        similar_pairs.append((u, v))
    print(f1(n, m, similar_pairs))
    print(f2(n, m, similar_pairs))

