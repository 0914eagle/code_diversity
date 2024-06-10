
def move_girls_in_front_of_boys(s):
    n = len(s)
    left_girl = 0
    right_boy = n - 1
    time_needed = 0

    while left_girl < right_boy:
        if s[left_girl] == 'F':
            left_girl += 1
        elif s[right_boy] == 'M':
            right_boy -= 1
        else:
            s[left_girl], s[right_boy] = s[right_boy], s[left_girl]
            left_girl += 1
            right_boy -= 1
            time_needed += 1

    return time_needed

if __name__ == '__main__':
    s = input().strip()
    print(move_girls_in_front_of_boys(list(s)))
