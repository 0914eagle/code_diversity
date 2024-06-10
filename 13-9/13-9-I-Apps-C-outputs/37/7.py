
def is_perfect(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if (s[i] ^ s[j]) not in s:
                return False
    return True

def count_perfect_sets(k):
    count = 0
    for i in range(k+1):
        s = [i]
        if is_perfect(s):
            count += 1
    return count % 1000000007

if __name__ == '__main__':
    k = int(input())
    print(count_perfect_sets(k))

