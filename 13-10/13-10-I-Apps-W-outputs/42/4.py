
import itertools

def get_period(s):
    for i in range(1, len(s)):
        if len(s) % i == 0:
            if all(s[j % len(s)] == s[j] for j in range(len(s))):
                return i
    return len(s)

def solve(a, b):
    periods = set()
    for i in range(a + b):
        for perm in itertools.permutations("A" * a + "B" * b):
            s = "".join(perm)
            periods.add(get_period(s))
    return len(periods)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(solve(a, b))

