
def is_even(s):
    return s == s[::-1]

def longest_even(s):
    if is_even(s):
        return len(s)
    
    for i in range(len(s)-1, 0, -1):
        if is_even(s[:i]):
            return i
    
    return 0

def main():
    s = input()
    print(longest_even(s))

if __name__ == '__main__':
    main()

