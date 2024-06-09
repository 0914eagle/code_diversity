
def compare_robots(k, a, b, alice_choices, bob_choices):
    alice_points, bob_points = 0, 0
    for i in range(k):
        if alice_choices[i] == bob_choices[i]:
            continue
        elif alice_choices[i] == a and bob_choices[i] == b:
            alice_points += 1
        elif alice_choices[i] == b and bob_choices[i] == a:
            bob_points += 1
    return alice_points, bob_points

