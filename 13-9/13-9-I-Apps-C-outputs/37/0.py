
def is_perfect(S):
    for a in S:
        for b in S:
            if a != b and (a ^ b) not in S:
                return False
    return True

def count_perfect_sets(k):
    count = 0
    for i in range(k+1):
        if is_perfect(set(range(i))):
            count += 1
    return count % 1000000007

if __name__ == '__main__':
    k = int(input())
    print(count_perfect_sets(k))

