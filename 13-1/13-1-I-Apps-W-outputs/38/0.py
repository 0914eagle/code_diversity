
def f1(n, a):
    # Initialize a list to store the roads
    roads = [0] * n
    for i in range(n):
        roads[i] = a[i]
    
    # Initialize a set to store the visited towns
    visited = set()
    
    # Initialize a variable to store the number of ways to flip the roads
    ways = 0
    
    # Iterate through each town
    for i in range(n):
        # If the town has not been visited before, visit it and flip the roads
        if i not in visited:
            ways += 1
            visited.add(i)
            while True:
                # If the current town is the destination town, break the loop
                if roads[i] == i:
                    break
                # Flip the road and move to the next town
                roads[i], roads[roads[i]] = roads[roads[i]], roads[i]
                i = roads[i]
    
    # Return the number of ways to flip the roads
    return ways

def f2(n, a):
    # Initialize a list to store the roads
    roads = [0] * n
    for i in range(n):
        roads[i] = a[i]
    
    # Initialize a set to store the visited towns
    visited = set()
    
    # Initialize a variable to store the number of ways to flip the roads
    ways = 0
    
    # Iterate through each town
    for i in range(n):
        # If the town has not been visited before, visit it and flip the roads
        if i not in visited:
            ways += 1
            visited.add(i)
            while True:
                # If the current town is the destination town, break the loop
                if roads[i] == i:
                    break
                # Flip the road and move to the next town
                roads[i], roads[roads[i]] = roads[roads[i]], roads[i]
                i = roads[i]
    
    # Return the number of ways to flip the roads
    return ways

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))
    print(f2(n, a))

