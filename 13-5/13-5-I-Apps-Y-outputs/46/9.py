
def get_input():
    return input()

def get_max_consecutive_rainy_days(s):
    max_count = 0
    current_count = 0
    for i in range(len(s)):
        if s[i] == "R":
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0
    return max(max_count, current_count)

def main():
    s = get_input()
    print(get_max_consecutive_rainy_days(s))

if __name__ == '__main__':
    main()

