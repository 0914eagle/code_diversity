
def solve(profit, pita_profit, pizza_profit):
    pitas = 0
    pizzas = 0
    while pitas * pita_profit + pizzas * pizza_profit < profit:
        pizzas += 1
        if pitas * pita_profit + pizzas * pizza_profit == profit:
            break
        if pitas * pita_profit + pizzas * pizza_profit > profit:
            pizzas -= 1
            pitas += 1
    return pitas, pizzas

