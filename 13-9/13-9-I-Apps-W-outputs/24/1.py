
def solve(n, a):
    # find the index of the last visited cafe
    last_visited = a[-1]
    # find the indices of all cafes visited before the last visited cafe
    before_last = [i for i in a if i < last_visited]
    # find the index of the cafe visited before the last visited cafe that is farthest from the last visited cafe
    farthest = max(before_last)
    # return the index of the cafe that hasn't been visited for as long as possible
    return farthest

