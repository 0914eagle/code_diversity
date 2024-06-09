
def solve(a):
    num_str = str(a)
    num_list = list(num_str)
    result = []
    for i in range(len(num_list)):
        if num_list[i] in '1689':
            result.append(num_list[i])
            num_list.remove(num_list[i])
    if len(result) == 4:
        return int(''.join(result))
    else:
        return 0

