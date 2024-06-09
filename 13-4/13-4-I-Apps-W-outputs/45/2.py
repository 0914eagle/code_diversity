
def count_permutations(n):
    def generate_permutations(n):
        if n == 1:
            yield [1]
        else:
            for i in range(1, n + 1):
                for perm in generate_permutations(n - 1):
                    yield [i] + perm
    
    def is_sum_of_two_permutations(p1, p2):
        for i in range(n):
            if (p1[i] + p2[i] - 2) % n == 0:
                return True
        return False
    
    count = 0
    for p1 in generate_permutations(n):
        for p2 in generate_permutations(n):
            if is_sum_of_two_permutations(p1, p2):
                count += 1
    
    return count % 1000000007

