
def f1(n, wishes):
    # Initialize a dictionary to store the count of each topping
    topping_count = {}

    # Iterate over the wishes of each friend
    for friend in wishes:
        # Iterate over the wishes of each friend
        for wish in friend:
            # If the wish is positive, increment the count of the topping
            if wish[0] == "+":
                topping = wish[1:]
                if topping not in topping_count:
                    topping_count[topping] = 1
                else:
                    topping_count[topping] += 1

    # Sort the toppings by count in descending order
    sorted_toppings = sorted(topping_count.items(), key=lambda x: x[1], reverse=True)

    # Return the top 3 toppings with the highest count
    return [topping for topping, count in sorted_toppings[:3]]

def f2(n, wishes):
    # Initialize a dictionary to store the count of each topping
    topping_count = {}

    # Iterate over the wishes of each friend
    for friend in wishes:
        # Iterate over the wishes of each friend
        for wish in friend:
            # If the wish is positive, increment the count of the topping
            if wish[0] == "+":
                topping = wish[1:]
                if topping not in topping_count:
                    topping_count[topping] = 1
                else:
                    topping_count[topping] += 1

    # Sort the toppings by count in descending order
    sorted_toppings = sorted(topping_count.items(), key=lambda x: x[1], reverse=True)

    # Return the top 3 toppings with the highest count
    return [topping for topping, count in sorted_toppings if count >= 2]

if __name__ == '__main__':
    n = int(input())
    wishes = []
    for _ in range(n):
        wishes.append(input().split())
    print(*f1(n, wishes))
    print(*f2(n, wishes))

