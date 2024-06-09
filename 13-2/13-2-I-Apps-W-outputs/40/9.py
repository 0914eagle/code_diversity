
def solve(queries):
    intervals = []
    for query in queries:
        if query[0] == 1:
            intervals.append((query[1], query[2]))
        else:
            for i in range(len(intervals)):
                if intervals[i][0] <= query[1] <= intervals[i][1] or intervals[i][0] <= query[2] <= intervals[i][1]:
                    print("YES")
                    break
            else:
                print("NO")

