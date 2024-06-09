
def f1(N, X, x_list):
    # find the minimum distance between X and any city
    min_dist = min([abs(X - x) for x in x_list])
    # find the maximum value of D that enables you to visit all the cities
    max_D = (N - 1) * min_dist
    return max_D

def f2(N, X, x_list):
    # sort the list of city coordinates in ascending order
    sorted_x_list = sorted(x_list)
    # find the minimum distance between any two cities
    min_dist = min([abs(x2 - x1) for x1, x2 in zip(sorted_x_list, sorted_x_list[1:])])
    # find the maximum value of D that enables you to visit all the cities
    max_D = (N - 1) * min_dist
    return max_D

if __name__ == '__main__':
    N, X = map(int, input().split())
    x_list = list(map(int, input().split()))
    print(f1(N, X, x_list))
    print(f2(N, X, x_list))

