
def get_maximum_fraction(balloons, canisters):
    # Sort the balloons and canisters in descending order
    balloons.sort(reverse=True)
    canisters.sort(reverse=True)
    
    # Initialize the maximum fraction as 0
    maximum_fraction = 0
    
    # Iterate through the balloons and canisters
    for balloon, canister in zip(balloons, canisters):
        # Check if the balloon is filled beyond its capacity
        if balloon > canister:
            return "impossible"
        
        # Calculate the fraction of the balloon that is filled
        fraction = canister / balloon
        
        # Update the maximum fraction
        maximum_fraction = max(maximum_fraction, fraction)
    
    return maximum_fraction

def main():
    balloons = list(map(int, input().split()))
    canisters = list(map(int, input().split()))
    print(get_maximum_fraction(balloons, canisters))

if __name__ == '__main__':
    main()

