
def get_largest_committee(N, K, book_of_great_achievements):
    # Initialize a set to store the committee members
    committee = set()
    # Loop through each politician and their disagreements
    for politician, disagreements in book_of_great_achievements.items():
        # If the politician is not in the committee yet, add them
        if politician not in committee:
            committee.add(politician)
            # Loop through the politician's disagreements
            for disagreement in disagreements:
                # If the disagreement is not in the committee yet, add them
                if disagreement not in committee:
                    committee.add(disagreement)
                    # If the size of the committee is greater than or equal to K, return the committee
                    if len(committee) >= K:
                        return len(committee)
    # If no committee of size K or greater is possible, return 0
    return 0

def main():
    N, K = map(int, input().split())
    book_of_great_achievements = {}
    for i in range(N):
        politician, num_disagreements = map(int, input().split())
        book_of_great_achievements[politician] = set(map(int, input().split()))
    print(get_largest_committee(N, K, book_of_great_achievements))

if __name__ == '__main__':
    main()

