
def is_possible_division(items, suspicious_pairs):
    graph = {}
    for item in items:
        graph[item] = set()
    
    for pair in suspicious_pairs:
        item1, item2 = pair.split()
        graph[item1].add(item2)
        graph[item2].add(item1)
    
    walters_items = set()
    jesses_items = set()
    
    for item in items:
        if item in walters_items or item in jesses_items:
            continue
        
        walters_items.add(item)
        stack = [item]
        while stack:
            current_item = stack.pop()
            for neighbor in graph[current_item]:
                if neighbor in walters_items:
                    return "impossible"
                jesses_items.add(neighbor)
                stack.append(neighbor)
    
    return walters_items, jesses_items

N = int(input())
items = [input() for _ in range(N)]
M = int(input())
suspicious_pairs = [input() for _ in range(M)]

result = is_possible_division(items, suspicious_pairs)
if result == "impossible":
    print("impossible")
else:
    walters_items, jesses_items = result
    print(" ".join(walters_items))
    print(" ".join(jesses_items))
