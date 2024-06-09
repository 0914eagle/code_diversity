
def solve(R, S, L, A, B):
    # Initialize a dictionary to store the number of lawsuits won by each individual and corporation
    counts = {}
    for i in range(1, R+1):
        counts[f"INDV {i}"] = 0
    for i in range(1, S+1):
        counts[f"CORP {i}"] = 0

    # Iterate through the lawsuits and increment the count for the party that wins each lawsuit
    for i in range(L):
        if A[i] not in counts:
            counts[f"INDV {A[i]}"] = 0
        if B[i] not in counts:
            counts[f"CORP {B[i]}"] = 0
        counts[f"INDV {A[i]}"] += 1
        counts[f"CORP {B[i]}"] += 1

    # Find the individual or corporation with the minimum number of lawsuits won
    min_count = min(counts.values())
    winners = [k for k, v in counts.items() if v == min_count]

    # Return the winners in the required format
    return [f"{winner}" for winner in winners]

