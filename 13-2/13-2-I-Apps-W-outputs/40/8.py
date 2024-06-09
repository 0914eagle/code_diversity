
def solve(queries):
    intervals = []
    for query in queries:
        if query[0] == 1:
            intervals.append((query[1], query[2]))
        elif query[0] == 2:
            for i in range(len(intervals)):
                if intervals[i][0] == query[1] and intervals[i][1] == query[2]:
                    print("YES")
                    break
            else:
                print("NO")

queries = [(1, 1, 5), (1, 5, 11), (2, 1, 2), (1, 2, 9), (2, 1, 2)]
solve(queries)

