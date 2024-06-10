
import math

def get_dog_behavior(A, B, C, D):
    # Calculate the total time the dogs spend being aggressive and calm
    aggressive_time = A + C
    calm_time = B + D
    
    # Calculate the total time the dogs spend in their behavior cycle
    total_time = aggressive_time + calm_time
    
    # Calculate the time elapsed since the last aggressive period started
    time_elapsed = math.fmod(total_time, aggressive_time)
    
    # Determine which dog is currently aggressive
    if time_elapsed < A:
        return "aggressive"
    else:
        return "calm"

def solve(A, B, C, D, P, M, G):
    # Get the behavior of each dog at the arrival time of each hero
    postman_dog_behavior = get_dog_behavior(A, B, C, D)
    milkman_dog_behavior = get_dog_behavior(A, B, C, D)
    garbage_man_dog_behavior = get_dog_behavior(A, B, C, D)
    
    # Determine how many dogs attack each hero
    postman_attacks = 0
    milkman_attacks = 0
    garbage_man_attacks = 0
    if postman_dog_behavior == "aggressive":
        postman_attacks += 1
    if milkman_dog_behavior == "aggressive":
        milkman_attacks += 1
    if garbage_man_dog_behavior == "aggressive":
        garbage_man_attacks += 1
    
    # Return the number of dogs that attack each hero
    return postman_attacks, milkman_attacks, garbage_man_attacks

def main():
    A, B, C, D = map(int, input().split())
    P, M, G = map(int, input().split())
    postman_attacks, milkman_attacks, garbage_man_attacks = solve(A, B, C, D, P, M, G)
    print("both" if postman_attacks == 2 else "one" if postman_attacks == 1 else "none")
    print("both" if milkman_attacks == 2 else "one" if milkman_attacks == 1 else "none")
    print("both" if garbage_man_attacks == 2 else "one" if garbage_man_attacks == 1 else "none")

if __name__ == '__main__':
    main()

