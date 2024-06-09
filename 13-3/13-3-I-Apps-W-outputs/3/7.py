
def f1(n, x, edges):
    # Calculate the greatest common divisor of two numbers
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    
    # Initialize the sum of beauties
    sum_beauties = 0
    
    # Iterate over all edges
    for edge in edges:
        # Get the vertices of the edge
        u, v = edge
        
        # Calculate the beauty of the path between u and v
        beauty = gcd(x[u], x[v])
        
        # Add the beauty to the sum of beauties
        sum_beauties += beauty
    
    # Return the sum of beauties modulo 10^9 + 7
    return sum_beauties % 1000000007

def f2(...):
    # Your code here
    pass

if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split()))
    edges = []
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f1(n, x, edges))

