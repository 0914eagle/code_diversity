
def get_toppings(n_friends, friend_wishes):
    # Initialize a dictionary to count the number of wishes for each topping
    topping_counts = {}
    for friend in friend_wishes:
        for wish in friend:
            if wish.startswith("+"):
                topping = wish[1:]
                if topping not in topping_counts:
                    topping_counts[topping] = 1
                else:
                    topping_counts[topping] += 1
    
    # Sort the toppings by their count in descending order
    sorted_toppings = sorted(topping_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Return the top 3 toppings with the highest count
    return [topping for topping, count in sorted_toppings[:3]]

def main():
    n_friends = int(input())
    friend_wishes = []
    for _ in range(n_friends):
        friend_wishes.append(input().split())
    print(*get_toppings(n_friends, friend_wishes), sep="\n")

if __name__ == '__main__':
    main()

