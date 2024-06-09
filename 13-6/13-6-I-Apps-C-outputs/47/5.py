
def count_perfect_sets(k):
    def is_perfect_set(s):
        for a in s:
            for b in s:
                if a != b and (a ^ b) not in s:
                    return False
        return True

    count = 0
    for i in range(k + 1):
        if is_perfect_set([i]):
            count += 1

    return count % 1000000007

