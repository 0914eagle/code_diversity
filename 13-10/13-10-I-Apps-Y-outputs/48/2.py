
def read_input():
    n = int(input())
    x = list(map(int, input().split()))
    return n, x

def get_distances(x):
    distances = []
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            distances.append(abs(x[i] - x[j]))
    return distances

def get_max_subset(x):
    distances = get_distances(x)
    max_subset = []
    for i in range(len(distances)):
        if distances[i] in [2, 4, 8, 16]:
            max_subset.append(i)
    return max_subset

def print_output(max_subset):
    print(len(max_subset))
    for i in max_subset:
        print(x[i], end=" ")

if __name__ == '__main__':
    n, x = read_input()
    max_subset = get_max_subset(x)
    print_output(max_subset)

