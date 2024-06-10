
def move_girls_in_front_of_boys(s):
    n = len(s)
    if 'F' not in s or 'M' not in s:
        return 0
    
    left_girl = 0
    right_boy = n - 1
    seconds = 0
    
    while left_girl < right_boy:
        if s[left_girl] == 'M' and s[right_boy] == 'F':
            s[left_girl], s[right_boy] = s[right_boy], s[left_girl]
            left_girl += 1
            right_boy -= 1
            seconds += 1
        elif s[left_girl] == 'F':
            left_girl += 1
        elif s[right_boy] == 'M':
            right_boy -= 1
    
    return seconds

if __name__ == '__main__':
    s = input().strip()
    print(move_girls_in_front_of_boys(list(s)))
