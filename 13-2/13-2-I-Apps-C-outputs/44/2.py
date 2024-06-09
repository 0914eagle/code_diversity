
def solve(queries):
    answers = []
    for query in queries:
        n, k = query
        if n == 0:
            answers.append('.')
        else:
            answers.append(f"What are you doing while sending \"What are you doing at the end of the world? Are you busy? Will you save us?\"? Are you busy? Will you send \"What are you doing at the end of the world? Are you busy? Will you save us?\"?")[k-1])
    return "".join(answers)

