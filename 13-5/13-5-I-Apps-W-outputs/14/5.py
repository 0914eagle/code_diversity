
def f1(n, m):
    # find the maximum height of towers made with two-block pieces
    max_height_two = (n * 2) + 1
    # find the maximum height of towers made with three-block pieces
    max_height_three = (m * 3) + 1
    # return the maximum of the two maximum heights
    return max(max_height_two, max_height_three)

def f2(n, m):
    # find the minimum height of towers made with two-block pieces
    min_height_two = n + 1
    # find the minimum height of towers made with three-block pieces
    min_height_three = m + 1
    # return the minimum of the two minimum heights
    return min(min_height_two, min_height_three)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(f1(n, m))

