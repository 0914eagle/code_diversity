
def f1(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Iterate through the disagreements and add the members to the committee
    for disagreement in disagreements:
        committee.update(disagreement)
    # Return the size of the committee
    return len(committee)

def f2(N, K, disagreements):
    # Initialize a set to store the members of the committee
    committee = set()
    # Iterate through the disagreements and add the members to the committee
    for disagreement in disagreements:
        committee.update(disagreement)
    # Return the size of the committee
    return len(committee)

if __name__ == '__main__':
    N, K = map(int, input().split())
    disagreements = []
    for i in range(N):
        D_i = int(input())
        disagreements.append(set(map(int, input().split())))
    print(f1(N, K, disagreements))
    print(f2(N, K, disagreements))

