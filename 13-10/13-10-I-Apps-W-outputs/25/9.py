
def get_min_time(n, m, c_l, c_e, v, queries):
    # Initialize a dictionary to store the minimum time needed to reach each section
    min_time = {}
    for i in range(1, n+1):
        for j in range(1, m+1):
            min_time[(i, j)] = float('inf')
    
    # Initialize a set to store the sections with guest rooms
    guest_rooms = set()
    for i in range(1, n+1):
        for j in range(1, m+1):
            if j not in c_l and j not in c_e:
                guest_rooms.add((i, j))
    
    # Breadth-first search to find the minimum time needed to reach each section
    queue = []
    queue.append((1, 1))
    min_time[(1, 1)] = 0
    while queue:
        current = queue.pop(0)
        current_time = min_time[current]
        for next in [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]:
            if next in guest_rooms and min_time[next] > current_time+1:
                min_time[next] = current_time+1
                queue.append(next)
    
    # Process the queries
    answers = []
    for query in queries:
        x1, y1, x2, y2 = query
        answers.append(min_time[(x1, y1)] + min_time[(x2, y2)] - 1)
    
    return answers

def main():
    n, m, c_l, c_e, v = map(int, input().split())
    c_l = set(map(int, input().split()))
    c_e = set(map(int, input().split()))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(tuple(map(int, input().split())))
    answers = get_min_time(n, m, c_l, c_e, v, queries)
    for answer in answers:
        print(answer)

if __name__ == '__main__':
    main()

