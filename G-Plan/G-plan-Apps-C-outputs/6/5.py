t_ways(n, m, q, runs, queries):
    ways = []
    
    for query in queries:
        k, a, *areas = query
        valid_ways = 0
        
        for i in range(1, n+1):
            if i in areas:
                valid_paths = 0
                for run in runs:
                    x, y = run
                    if x == 1 and y == i:
                        valid_paths += 1
                if valid_paths == 1:
                    valid_ways += 1
        
        ways.append(valid_ways)
    
    return ways

if __name__ == "__main__":
    n, m, q = map(int, input().split())
    runs = [tuple(map(int, input().split())) for _ in range(m)]
    queries = [list(map(int, input().split())) for _ in range(q)]
    
    result = count_ways(n, m, q, runs, queries)
    for res in result:
        print(res