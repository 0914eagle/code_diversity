
def move_girls_in_front_of_boys(s):
    n = len(s)
    if 'F' not in s or 'M' not in s:
        return 0
    
    left_girl = 0
    right_boy = n - 1
    time_needed = 0
    
    while left_girl < right_boy:
        if s[left_girl] == 'M' and s[right_boy] == 'F':
            s[left_girl], s[right_boy] = s[right_boy], s[left_girl]
            time_needed += 1
        
        if s[left_girl] == 'F':
            left_girl += 1
        if s[right_boy] == 'M':
            right_boy -= 1
    
    return time_needed

if __name__ == '__main__':
    s = input().strip()
    s = list(s)
    result = move_girls_in_front_of_boys(s)
    print(result)