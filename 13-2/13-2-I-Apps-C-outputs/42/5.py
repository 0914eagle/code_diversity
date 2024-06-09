
def get_max_beauty(n):
    def beauty(p):
        return sum(i ^ p[i] for i in range(n+1))
    return max(itertools.permutations(range(n+1)), key=beauty)

