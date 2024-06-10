
def get_intersections(n):
    intersections = []
    for i in range(n):
        intersection = input().split()
        intersections.append(intersection)
    return intersections

def get_correct_intersection(intersections, alice_intersection, bob_intersection):
    for i in range(len(intersections)):
        if intersections[i][0] == alice_intersection and intersections[i][1] == bob_intersection:
            return i
    return -1

def get_number_of_turns(intersections, alice_intersection, bob_intersection):
    correct_intersection = get_correct_intersection(intersections, alice_intersection, bob_intersection)
    if correct_intersection == -1:
        return "indistinguishable"
    
    alice_turns = 0
    bob_turns = 0
    current_intersection = alice_intersection
    while current_intersection != correct_intersection:
        if current_intersection == alice_intersection:
            current_intersection = intersections[current_intersection][1]
            alice_turns += 1
        else:
            current_intersection = intersections[current_intersection][0]
            bob_turns += 1
    
    return min(alice_turns, bob_turns)

def main():
    n, alice_intersection, bob_intersection = map(int, input().split())
    intersections = get_intersections(n)
    print(get_number_of_turns(intersections, alice_intersection, bob_intersection))

if __name__ == '__main__':
    main()

