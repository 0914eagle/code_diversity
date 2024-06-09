
def get_toppings(n, friends):
    # Initialize a dictionary to store the toppings and their counts
    toppings = {}
    for friend in friends:
        # Iterate over the friend's wishes and update the toppings dictionary
        for wish in friend:
            if wish[0] == "+":
                toppings[wish[1:]] = toppings.get(wish[1:], 0) + 1
            else:
                toppings[wish[1:]] = toppings.get(wish[1:], 0) - 1
    
    # Initialize a list to store the selected toppings
    selected_toppings = []
    # Iterate over the toppings dictionary and select the toppings with the highest count
    for topping, count in toppings.items():
        if count > 0:
            selected_toppings.append(topping)
    
    return selected_toppings

def main():
    n = int(input())
    friends = []
    for i in range(n):
        friends.append(input().split())
    selected_toppings = get_toppings(n, friends)
    print(*selected_toppings, sep="\n")

if __name__ == '__main__':
    main()

