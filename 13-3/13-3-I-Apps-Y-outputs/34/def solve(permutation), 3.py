
def solve(permutation):
    n = len(permutation)
    # Swap the first and second elements if the first element is greater than the second element
    if permutation[0] > permutation[1]:
        permutation[0], permutation[1] = permutation[1], permutation[0]
    # Swap the second and third elements if the second element is greater than the third element
    if permutation[1] > permutation[2]:
        permutation[1], permutation[2] = permutation[2], permutation[1]
    # Swap the third and fourth elements if the third element is greater than the fourth element
    if permutation[2] > permutation[3]:
        permutation[2], permutation[3] = permutation[3], permutation[2]
    # Swap the fourth and fifth elements if the fourth element is greater than the fifth element
    if permutation[3] > permutation[4]:
        permutation[3], permutation[4] = permutation[4], permutation[3]
    return " ".join(str(i) for i in permutation)

