
def get_finish_time(queries, b):
    
    finish_time = []
    queue = []
    for query in queries:
        t, d = query
        if not queue and not finish_time:
            finish_time.append(t + d)
        elif len(queue) < b:
            queue.append(query)
        else:
            finish_time.append(-1)
    
    while queue:
        query = queue.pop(0)
        t, d = query
        finish_time.append(t + d)
    
    return finish_time

def main():
    n, b = map(int, input().split())
    queries = []
    for _ in range(n):
        queries.append(list(map(int, input().split())))
    finish_time = get_finish_time(queries, b)
    print(*finish_time, sep='\n')

if __name__ == '__main__':
    main()

