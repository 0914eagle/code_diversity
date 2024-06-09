
def get_balanced_ternary_string(s):
    n = len(s)
    count = [s.count(i) for i in '012']
    diff = max(count) - min(count)
    if diff > 1:
        return '-1'
    
    count_0 = count[0]
    count_1 = count[1]
    count_2 = count[2]
    
    if count_0 > count_1:
        s = s.replace('0', '1', count_0 - count_1)
    elif count_1 > count_0:
        s = s.replace('1', '0', count_1 - count_0)
    
    if count_1 > count_2:
        s = s.replace('1', '2', count_1 - count_2)
    elif count_2 > count_1:
        s = s.replace('2', '1', count_2 - count_1)
    
    return s

