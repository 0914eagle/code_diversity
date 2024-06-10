
def predict_dogs_behavior(aggressive_minutes, calm_minutes):
    aggressive_periods = [i for i in range(aggressive_minutes[0], aggressive_minutes[1]+1)]
    calm_periods = [i for i in range(calm_minutes[0], calm_minutes[1]+1)]
    return aggressive_periods, calm_periods

def detect_dog_attacks(postman_arrival, milkman_arrival, garbage_man_arrival, aggressive_periods, calm_periods):
    postman_attacks = 0
    milkman_attacks = 0
    garbage_man_attacks = 0
    if postman_arrival in aggressive_periods:
        postman_attacks += 1
    if milkman_arrival in aggressive_periods:
        milkman_attacks += 1
    if garbage_man_arrival in aggressive_periods:
        garbage_man_attacks += 1
    if postman_arrival in calm_periods:
        postman_attacks -= 1
    if milkman_arrival in calm_periods:
        milkman_attacks -= 1
    if garbage_man_arrival in calm_periods:
        garbage_man_attacks -= 1
    return postman_attacks, milkman_attacks, garbage_man_attacks

def main():
    aggressive_minutes = list(map(int, input().split()))
    calm_minutes = list(map(int, input().split()))
    postman_arrival, milkman_arrival, garbage_man_arrival = list(map(int, input().split()))
    aggressive_periods, calm_periods = predict_dogs_behavior(aggressive_minutes, calm_minutes)
    postman_attacks, milkman_attacks, garbage_man_attacks = detect_dog_attacks(postman_arrival, milkman_arrival, garbage_man_arrival, aggressive_periods, calm_periods)
    print("both" if postman_attacks > 0 and milkman_attacks > 0 and garbage_man_attacks > 0 else "one" if postman_attacks > 0 or milkman_attacks > 0 or garbage_man_attacks > 0 else "none")

if __name__ == '__main__':
    main()

