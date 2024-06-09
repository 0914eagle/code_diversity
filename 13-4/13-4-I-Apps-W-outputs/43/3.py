
def get_answer(names):
    seen = set()
    answer = []
    for name in names:
        if name in seen:
            answer.append("YES")
        else:
            answer.append("NO")
            seen.add(name)
    return answer

