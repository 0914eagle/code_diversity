
def get_toppings(n_friends, friends_wishes):
    # Initialize a dictionary to count the number of wishes for each topping
    topping_count = {}
    for friend in friends_wishes:
        for wish in friend:
            if wish[0] == "+":
                topping = wish[1:]
                if topping not in topping_count:
                    topping_count[topping] = 1
                else:
                    topping_count[topping] += 1
    
    # Sort the toppings by their count in descending order
    sorted_toppings = sorted(topping_count.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top 3 toppings with the highest count
    return [topping for topping, count in sorted_toppings[:3]]

def main():
    n_friends = int(input())
    friends_wishes = []
    for _ in range(n_friends):
        friends_wishes.append(input().split())
    print(*get_toppings(n_friends, friends_wishes), sep="\n")

if __name__ == "__main__":
    main()

