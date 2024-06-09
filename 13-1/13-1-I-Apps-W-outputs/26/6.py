
def compare_robots(k, a, b, A, B):
    alice_points = 0
    bob_points = 0

    for i in range(k):
        if A[i] == B[i]:
            continue
        elif A[i] == a and B[i] == b:
            alice_points += 1
        elif A[i] == b and B[i] == a:
            bob_points += 1

    return alice_points, bob_points

