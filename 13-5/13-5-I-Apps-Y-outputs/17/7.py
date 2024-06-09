
def get_min_mp(N, A, B, C, l_list):
    # Initialize the minimum MP needed to achieve the objective
    min_mp = 0

    # Initialize the list of bamboos
    bamboos = l_list[:]

    # Sort the list of bamboos in descending order
    bamboos.sort(reverse=True)

    # Use Extension Magic to increase the length of the bamboos
    for i in range(N):
        if bamboos[i] < A:
            min_mp += 1
            bamboos[i] += 1

    # Use Shortening Magic to decrease the length of the bamboos
    for i in range(N):
        if bamboos[i] > B:
            min_mp += 1
            bamboos[i] -= 1

    # Use Composition Magic to combine the bamboos
    for i in range(N-1):
        for j in range(i+1, N):
            if bamboos[i] + bamboos[j] == C:
                min_mp += 10
                bamboos[i] = bamboos[i] + bamboos[j]
                bamboos.pop(j)
                break

    return min_mp

def main():
    N, A, B, C = map(int, input().split())
    l_list = list(map(int, input().split()))
    print(get_min_mp(N, A, B, C, l_list))

if __name__ == '__main__':
    main()

