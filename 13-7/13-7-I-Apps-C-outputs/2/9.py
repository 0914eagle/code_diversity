
def solve(transcript):
    N, K = map(int, input().split())
    candidates = [[] for _ in range(N)]
    for _ in range(K):
        speaker, statement = input().split()
        candidates[int(speaker) - 1].append(statement)
    types = []
    for candidate in candidates:
        truths = [s for s in candidate if s.startswith(("truther", "fabulist", "charlatan"))]
        if len(truths) == 0:
            types.append("truther")
        elif len(truths) == 1:
            types.append(truths[0].split()[0])
        else:
            types.append("charlatan")
    return "\n".join(types)

