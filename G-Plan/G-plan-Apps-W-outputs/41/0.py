
def time_to_rearrange_queue(s):
    boys = 0
    girls = 0
    for char in s:
        if char == 'M':
            boys += 1
        else:
            girls += 1
    
    if boys == 0 or girls == 0:
        return 0
    
    left_girl = 0
    right_boy = len(s) - 1
    time = 0
    
    while left_girl < right_boy:
        if s[left_girl] == 'F' and s[right_boy] == 'M':
            left_girl += 1
            right_boy -= 1
        elif s[left_girl] == 'M':
            right_boy -= 1
        elif s[right_boy] == 'F':
            left_girl += 1
        time += 1
    
    return time

if __name__ == '__main__':
    s = input().strip()
    print(time_to_rearrange_queue(s))
