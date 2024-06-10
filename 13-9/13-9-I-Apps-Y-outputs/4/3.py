
def get_party_day(tree_days):
    # Sort the list of tree days in ascending order
    tree_days.sort()
    # The party can be organized after the last tree has grown, which is the last element of the list
    return tree_days[-1] + 1

def main():
    n = int(input())
    tree_days = list(map(int, input().split()))
    print(get_party_day(tree_days))

if __name__ == '__main__':
    main()

