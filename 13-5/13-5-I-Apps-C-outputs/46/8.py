
def solve(N, queries):
    students = []
    for query in queries:
        if query.startswith("D"):
            A, B = map(int, query.split()[1:])
            students.append((A, B))
        else:
            i = int(query.split()[1]) - 1
            for j, (A, B) in enumerate(students):
                if A >= students[i][0] and B >= students[i][1]:
                    print(j + 1)
                    break
            else:
                print("NE")

