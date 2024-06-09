
def f1(N, X, x_list):
    # find the minimum distance between X and any city
    min_dist = float('inf')
    for x in x_list:
        dist = abs(X - x)
        if dist < min_dist:
            min_dist = dist
    
    # return the maximum value of D that is greater than or equal to the minimum distance
    return max(min_dist, 1)

def f2(N, X, x_list):
    # sort the list of cities in ascending order
    x_list.sort()
    
    # find the maximum value of D that enables you to visit all the cities
    D = 1
    while D <= X:
        # check if all cities are visited
        visited = [False] * N
        for i in range(N):
            if x_list[i] - X >= D:
                visited[i] = True
            elif X - x_list[i] >= D:
                visited[i] = True
        if all(visited):
            break
        D += 1
    
    return D

if __name__ == '__main__':
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    print(f2(N, X, x_list))

