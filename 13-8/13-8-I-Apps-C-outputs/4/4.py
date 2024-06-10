
def is_possible(N, parents, weights):
    # Initialize a dictionary to store the color and weight of each vertex
    colors = {}
    for i in range(1, N+1):
        colors[i] = "white"
    for i in range(1, N+1):
        colors[i] = "black"
    
    # Initialize a dictionary to store the total weight of each color
    total_weights = {"white": 0, "black": 0}
    
    # Loop through each vertex and its descendants and update the total weight of each color
    for i in range(1, N+1):
        for j in range(i, N+1):
            if parents[j] == i:
                total_weights[colors[i]] += weights[j]
    
    # Check if the total weight of each color is equal to the corresponding value in the favorite sequence
    for i in range(1, N+1):
        if total_weights[colors[i]] != weights[i]:
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

def main():
    N = int(input())
    parents = list(map(int, input().split()))
    weights = list(map(int, input().split()))
    print(is_possible(N, parents, weights))

if __name__ == '__main__':
    main()

