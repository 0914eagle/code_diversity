
def get_ranks(points):
    # Sort the points in descending order
    points.sort(reverse=True)
    # Initialize the ranks as the index of the point in the sorted list + 1
    ranks = [i + 1 for i in range(len(points))]
    # Loop through the points and update the ranks accordingly
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if points[i] == points[j]:
                ranks[i] = ranks[j]
    return ranks

def get_highest_and_lowest_place(points, ranks):
    # Get the highest place by finding the index of the maximum rank in the ranks list
    highest_place = ranks.index(max(ranks)) + 1
    # Get the lowest place by finding the index of the minimum rank in the ranks list
    lowest_place = ranks.index(min(ranks)) + 1
    return highest_place, lowest_place

def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))
    ranks = get_ranks(points)
    for i in range(N):
        highest_place, lowest_place = get_highest_and_lowest_place(points[i], ranks)
        print(highest_place, lowest_place)

if __name__ == '__main__':
    main()

