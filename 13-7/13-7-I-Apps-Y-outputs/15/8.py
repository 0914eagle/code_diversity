
def solve(s, t):
    s_list = list(s)
    t_list = list(t)
    if len(s_list) < len(t_list):
        return "Yes"
    if len(s_list) > len(t_list):
        return "No"
    for i in range(len(s_list)):
        if s_list[i] < t_list[i]:
            return "Yes"
        elif s_list[i] > t_list[i]:
            return "No"
    return "Yes"

