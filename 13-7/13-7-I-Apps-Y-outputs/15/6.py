
def solve(s, t):
    s_arr = list(s)
    t_arr = list(t)
    s_arr.sort()
    t_arr.sort()
    if s_arr == t_arr:
        return "Yes"
    for i in range(len(s_arr)):
        if s_arr[i] < t_arr[i]:
            return "Yes"
    return "No"

