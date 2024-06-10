
def is_perfect(s, k):
    # Function to check if a set is perfect
    for i in range(k+1):
        for j in range(i+1, k+1):
            if (i ^ j) not in s:
                return False
    return True

def count_perfect_sets(k):
    # Function to count the number of perfect sets
    count = 0
    for i in range(k+1):
        s = set([i])
        if is_perfect(s, k):
            count += 1
    return count

if __name__ == '__main__':
    k = int(input())
    print(count_perfect_sets(k) % 1000000007)

