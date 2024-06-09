
def f1(N, K):
    # Initialize a list to store the disagreements between politicians
    disagreements = []

    # Iterate through the input and add the disagreements to the list
    for i in range(N):
        disagreements.append(list(map(int, input().split())))

    # Initialize a set to store the members of the committee
    committee = set()

    # Iterate through the disagreements and add the members to the committee
    for i in range(N):
        for j in range(i+1, N):
            if disagreements[i][j] == 1:
                committee.add(i)
                committee.add(j)

    # Return the size of the committee
    return len(committee)

def f2(N, K):
    # Initialize a list to store the disagreements between politicians
    disagreements = []

    # Iterate through the input and add the disagreements to the list
    for i in range(N):
        disagreements.append(list(map(int, input().split())))

    # Initialize a set to store the members of the committee
    committee = set()

    # Iterate through the disagreements and add the members to the committee
    for i in range(N):
        for j in range(i+1, N):
            if disagreements[i][j] == 1:
                committee.add(i)
                committee.add(j)

    # Return the size of the committee
    return len(committee)

if __name__ == '__main__':
    N, K = map(int, input().split())
    print(f1(N, K))
    print(f2(N, K))

