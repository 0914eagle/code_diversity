
def get_dog_attack_time(aggressive_time, calm_time):
    # Calculate the total time the dog is aggressive and calm
    total_aggressive_time = aggressive_time + calm_time
    total_time = aggressive_time + calm_time
    
    # Calculate the time the dog is aggressive and calm in a day
    aggressive_time_per_day = total_aggressive_time * 2
    calm_time_per_day = total_time - aggressive_time_per_day
    
    # Calculate the time the dog is aggressive and calm in a minute
    aggressive_time_per_minute = aggressive_time_per_day / total_time
    calm_time_per_minute = calm_time_per_day / total_time
    
    return aggressive_time_per_minute, calm_time_per_minute

def get_dog_attack(aggressive_time_per_minute, calm_time_per_minute, arrival_time):
    # Calculate the time the dog is aggressive and calm at the arrival time
    aggressive_time = aggressive_time_per_minute * arrival_time
    calm_time = calm_time_per_minute * arrival_time
    
    # Check if the dog is aggressive or calm at the arrival time
    if aggressive_time >= calm_time:
        return "one"
    else:
        return "none"

def main():
    # Read the input
    aggressive_time, calm_time, arrival_time = map(int, input().split())
    
    # Calculate the time the dog is aggressive and calm
    aggressive_time_per_minute, calm_time_per_minute = get_dog_attack_time(aggressive_time, calm_time)
    
    # Calculate the dog attack at the arrival time
    dog_attack = get_dog_attack(aggressive_time_per_minute, calm_time_per_minute, arrival_time)
    
    # Print the output
    print(dog_attack)

if __name__ == '__main__':
    main()

