
def concatenate(s, n):
    return s * n

def count_substring(s, t):
    count = 0
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            count += 1
    return count

def main():
    n = int(input())
    t = input()
    s = concatenate("110", 10**10)
    print(count_substring(s, t))

if __name__ == '__main__':
    main()

