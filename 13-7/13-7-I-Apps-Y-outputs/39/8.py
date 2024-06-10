
def is_even_string(s):
    return s == s[::-1]

def longest_even_string(s):
    for i in range(len(s), 0, -1):
        if is_even_string(s[:i]):
            return i

def main():
    s = input()
    print(longest_even_string(s))

if __name__ == '__main__':
    main()

