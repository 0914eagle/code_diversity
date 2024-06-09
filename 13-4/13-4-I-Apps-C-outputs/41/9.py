
import sys
import math

def get_input():
    n = int(input())
    edges = []
    for i in range(n-1):
        a, b = map(int, input().split())
        edges.append((a, b))
    return n, edges

def paint_graph(n, edges):
    # Initialize the graph with all vertices as white
    graph = [0] * (n+1)

    # Paint the vertices according to the given edges
    for edge in edges:
        graph[edge[0]] = 1
        graph[edge[1]] = 1

    # Calculate the niceness of the painting
    niceness = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if graph[i] == graph[j]:
                niceness = max(niceness, abs(i-j))

    return niceness

def f1(n, edges):
    # Calculate the number of ways to paint the graph
    num_ways = math.pow(2, n)

    # Calculate the niceness of each way of painting the graph
    nicenesses = []
    for i in range(num_ways):
        # Convert the integer i to a binary string
        binary_string = bin(i)[2:]
        binary_string = binary_string.zfill(n)

        # Convert the binary string to a list of 0s and 1s
        painting = []
        for char in binary_string:
            painting.append(int(char))

        # Paint the graph according to the painting
        graph = paint_graph(n, edges)

        # Calculate the niceness of the painting
        niceness = paint_graph(n, edges)

        # Add the niceness to the list of nicenesses
        nicenesses.append(niceness)

    # Calculate the sum of the nicenesses
    sum_nicenesses = sum(nicenesses)

    # Return the sum of the nicenesses modulo (10^9+7)
    return sum_nicenesses % (10**9+7)

def f2(n, edges):
    # Calculate the number of ways to paint the graph
    num_ways = math.pow(2, n)

    # Calculate the niceness of each way of painting the graph
    nicenesses = []
    for i in range(num_ways):
        # Convert the integer i to a binary string
        binary_string = bin(i)[2:]
        binary_string = binary_string.zfill(n)

        # Convert the binary string to a list of 0s and 1s
        painting = []
        for char in binary_string:
            painting.append(int(char))

        # Paint the graph according to the painting
        graph = paint_graph(n, edges)

        # Calculate the niceness of the painting
        niceness = paint_graph(n, edges)

        # Add the niceness to the list of nicenesses
        nicenesses.append(niceness)

    # Calculate the sum of the nicenesses
    sum_nicenesses = sum(nicenesses)

    # Return the sum of the nicenesses modulo (10^9+7)
    return sum_nicenesses % (10**9+7)

if __name__ == '__main__':
    n, edges = get_input()
    print(f1(n, edges))
    print(f2(n, edges))

