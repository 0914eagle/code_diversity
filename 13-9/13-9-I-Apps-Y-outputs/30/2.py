
import math

def determine_dog_attack(arrival_time, agressive_minutes, calm_minutes):
    # Calculate the number of aggressive and calm minutes before the arrival time
    aggressive_minutes_before = math.floor(arrival_time / agressive_minutes) * agressive_minutes
    calm_minutes_before = math.floor(arrival_time / calm_minutes) * calm_minutes
    
    # Calculate the number of aggressive and calm minutes after the arrival time
    aggressive_minutes_after = agressive_minutes - aggressive_minutes_before
    calm_minutes_after = calm_minutes - calm_minutes_before
    
    # Determine if the dogs will attack during the arrival time
    if aggressive_minutes_before < arrival_time <= aggressive_minutes_before + aggressive_minutes:
        return "one"
    elif aggressive_minutes_before < arrival_time <= aggressive_minutes_before + aggressive_minutes + calm_minutes:
        return "none"
    elif aggressive_minutes_after < arrival_time <= aggressive_minutes_after + calm_minutes:
        return "none"
    else:
        return "one"

def main():
    a, b, c, d = map(int, input().split())
    p, m, g = map(int, input().split())
    
    print(determine_dog_attack(p, a, b))
    print(determine_dog_attack(m, c, d))
    print(determine_dog_attack(g, a, b))

if __name__ == '__main__':
    main()

