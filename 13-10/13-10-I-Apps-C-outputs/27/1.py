
def get_pairwise_distances(universities, n, k):
    
    distances = []
    for i in range(k):
        for j in range(i+1, k):
            distance = 0
            for university in universities:
                if university[i] != university[j]:
                    distance += 1
            distances.append(distance)
    return distances

def get_max_distance(universities, n, k):
    
    distances = get_pairwise_distances(universities, n, k)
    return max(distances)

def main():
    n, k = map(int, input().split())
    universities = []
    for _ in range(k):
        universities.append(list(map(int, input().split())))
    print(get_max_distance(universities, n, k))

if __name__ == '__main__':
    main()

