
def max_distance(towns, pairs, universities, roads):
    sorted_universities = sorted(universities)
    distances = []
    
    for i in range(0, len(sorted_universities), 2):
        distances.append(abs(sorted_universities[i] - sorted_universities[i+1]))
    
    distances.sort(reverse=True)
    return sum(distances[:pairs])

if __name__ == "__main__":
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = [list(map(int, input().split())) for _ in range(n-1)]
    
    print(max_distance(n, k, universities, roads))
