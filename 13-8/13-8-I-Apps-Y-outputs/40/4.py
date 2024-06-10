
def is_periodic(s, k):
    if len(s) % k != 0:
        return False
    for i in range(len(s) // k):
        if s[i*k:(i+1)*k] != s[(i+1)*k:(i+2)*k]:
            return False
    return True

def find_smallest_period(s):
    for k in range(1, len(s)):
        if is_periodic(s, k):
            return k
    return 0

if __name__ == '__main__':
    s = input()
    print(find_smallest_period(s))

