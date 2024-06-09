
def solve(h_list, k):
    h_list.sort()
    return h_list[-k] - h_list[k-1]

