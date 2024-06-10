
def get_input():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    return k, n, a

def solve(k, n, a):
    # Calculate the sum of the distances between each pair of houses
    distances = [0] * n
    for i in range(n):
        distances[i] = abs(a[(i+1)%n] - a[i])
    
    # Find the minimum distance by finding the minimum element in the distances list
    return min(distances)

def main():
    k, n, a = get_input()
    print(solve(k, n, a))

if __name__ == '__main__':
    main()

