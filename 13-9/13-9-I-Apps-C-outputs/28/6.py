
def get_distances(n, u_list):
    distances = []
    for i in range(n):
        for j in range(i+1, n):
            if i != j:
                distances.append(abs(u_list[i] - u_list[j]))
    return distances

def get_maximum_distance(distances):
    return max(distances)

def get_universities_pairs(n, k):
    u_list = []
    for i in range(k):
        u_list.append(i+1)
    return u_list

def get_total_distance(u_list, distances):
    total_distance = 0
    for i in range(len(u_list)):
        for j in range(i+1, len(u_list)):
            total_distance += distances[abs(u_list[i] - u_list[j])-1]
    return total_distance

def main():
    n, k = map(int, input().split())
    u_list = get_universities_pairs(n, k)
    distances = get_distances(n, u_list)
    maximum_distance = get_maximum_distance(distances)
    total_distance = get_total_distance(u_list, distances)
    print(total_distance)

if __name__ == '__main__':
    main()

