
def read_input(n):
    
    a = []
    b = []
    c = []
    for _ in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
    return a, b, c

def get_weighting_formula(a, b, c):
    
    # sort the data by the measure a_i * S + b_i * T
    sorted_data = sorted(zip(a, b, c), key=lambda x: x[0] * S + x[1] * T)

    # find the indices of the first and last elements with c_i true
    j = 0
    k = 0
    for i, (a_i, b_i, c_i) in enumerate(sorted_data):
        if c_i:
            j = i
            break
    for i, (a_i, b_i, c_i) in enumerate(reversed(sorted_data)):
        if c_i:
            k = len(sorted_data) - i - 1
            break

    # return the cluster size
    return k - j + 1

def main():
    # read the input data
    n = int(input())
    a, b, c = read_input(n)

    # find the smallest possible cluster size over all possible (S, T) pairs
    smallest_cluster_size = float('inf')
    for S in range(1, 2000001):
        for T in range(1, 2000001):
            cluster_size = get_weighting_formula(a, b, c)
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size

    # output the result
    print(smallest_cluster_size)

if __name__ == '__main__':
    main()

