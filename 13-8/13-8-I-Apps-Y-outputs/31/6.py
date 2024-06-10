
def reverse_string(s):
    return s[::-1]

def solve(s):
    s = reverse_string(s)
    s = s.replace("<", "")
    s = reverse_string(s)
    return s

if __name__ == '__main__':
    s = input()
    print(solve(s))

