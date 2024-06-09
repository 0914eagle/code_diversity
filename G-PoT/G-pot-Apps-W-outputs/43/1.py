
def max_annoyance_level(h, c, coworkers):
    coworkers.sort(key=lambda x: x[1], reverse=True)
    total_annoyance = 0

    for i in range(h):
        total_annoyance += coworkers[i % c][0]
        coworkers[i % c] = (coworkers[i % c][0] + coworkers[i % c][1], coworkers[i % c][1])

    return max([coworker[0] for coworker in coworkers])

# Input processing
h, c = map(int, input().split())
coworkers = [tuple(map(int, input().split())) for _ in range(c)]

# Call the function and print the output
print(max_annoyance_level(h, c, coworkers))
