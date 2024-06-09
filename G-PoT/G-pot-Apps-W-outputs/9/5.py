
def restore_object():
    n, m, h = map(int, input().split())
    front_view = list(map(int, input().split()))
    left_view = list(map(int, input().split()))
    
    top_view = []
    for _ in range(n):
        top_view.append(list(map(int, input().split())))
    
    result = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            result[i][j] = min(front_view[j], left_view[i], h) if top_view[i][j] == 1 else 0
    
    for row in result:
        print(' '.join(map(str, row)))

restore_object()
