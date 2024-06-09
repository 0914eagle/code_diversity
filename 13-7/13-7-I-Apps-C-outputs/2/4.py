
def solve(transcript):
    N, K = map(int, transcript[0].split())
    candidates = {}
    for i in range(1, K+1):
        speaker, statement = transcript[i].split()
        speaker = int(speaker)
        if statement.startswith("truther"):
            candidates[speaker] = "truther"
        elif statement.startswith("fabulist"):
            candidates[speaker] = "fabulist"
        elif statement.startswith("charlatan"):
            candidates[speaker] = "charlatan"
        elif statement.startswith("not"):
            operand = statement.split(" ")[1]
            if operand in candidates:
                candidates[speaker] = "truther" if candidates[operand] == "fabulist" else "fabulist"
        elif statement.startswith("and"):
            operands = statement.split(" ")[1:]
            if all(operand in candidates for operand in operands):
                candidates[speaker] = "truther" if all(candidates[operand] == "truther" for operand in operands) else "fabulist"
        elif statement.startswith("xor"):
            operands = statement.split(" ")[1:]
            if all(operand in candidates for operand in operands):
                candidates[speaker] = "truther" if candidates[operands[0]] != candidates[operands[1]] else "fabulist"
    return [candidates[i] for i in range(1, N+1)]

