
def get_cut_cost(A, B):
    # Find the shortest edge of polygon B that is incident to polygon A
    shortest_edge_idx = 0
    shortest_edge_len = float('inf')
    for i in range(len(B)):
        edge_len = get_edge_len(B, i)
        if edge_len < shortest_edge_len:
            shortest_edge_idx = i
            shortest_edge_len = edge_len
    
    # Cut polygon A along the shortest edge of polygon B
    cut_cost = shortest_edge_len
    cut_vertices = []
    for i in range(shortest_edge_idx, shortest_edge_idx + len(B)):
        cut_vertices.append(B[i % len(B)])
    
    # Find the remaining polygon that contains polygon B
    remaining_polygon = []
    for vertex in A:
        if vertex not in cut_vertices:
            remaining_polygon.append(vertex)
    
    # Recursively call the function to find the minimum cost for the remaining polygon
    if len(remaining_polygon) > 0:
        cut_cost += get_cut_cost(remaining_polygon, B)
    
    return cut_cost

def get_edge_len(polygon, idx):
    return ((polygon[idx][0] - polygon[(idx + 1) % len(polygon)][0]) ** 2 + (polygon[idx][1] - polygon[(idx + 1) % len(polygon)][1]) ** 2) ** 0.5

def read_input():
    A = []
    B = []
    num_vertices_A = int(input())
    for i in range(num_vertices_A):
        x, y = map(int, input().split())
        A.append((x, y))
    num_vertices_B = int(input())
    for i in range(num_vertices_B):
        x, y = map(int, input().split())
        B.append((x, y))
    return A, B

if __name__ == '__main__':
    A, B = read_input()
    print(get_cut_cost(A, B))

