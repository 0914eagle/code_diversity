
def is_periodic(s, k):
    if len(s) % k != 0:
        return False
    for i in range(len(s) // k):
        if s[i * k:i * k + k] != s[i * k + 1:i * k + k + 1] + s[i * k:i * k + 1]:
            return False
    return True

def get_smallest_period(s):
    for k in range(1, len(s)):
        if is_periodic(s, k):
            return k
    return len(s)

if __name__ == '__main__':
    s = input()
    print(get_smallest_period(s))

