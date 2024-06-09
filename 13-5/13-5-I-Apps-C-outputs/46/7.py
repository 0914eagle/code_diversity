
def solve(N, queries):
    students = []
    for query in queries:
        if query.startswith("D"):
            A, B = map(int, query.split()[1:])
            students.append((A, B))
        else:
            i = int(query.split()[1])
            best_student = -1
            min_diff = float('inf')
            for j, (A, B) in enumerate(students):
                if A >= students[i-1][0] and B >= students[i-1][1]:
                    diff = abs(A - students[i-1][0]) + abs(B - students[i-1][1])
                    if diff < min_diff:
                        min_diff = diff
                        best_student = j+1
            print(best_student if best_student != -1 else "NE")

