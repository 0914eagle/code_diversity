
def get_leftover_juice(amounts, ratios):
    orange_amount, apple_amount, pineapple_amount = amounts
    orange_ratio, apple_ratio, pineapple_ratio = ratios
    
    total_ratio = orange_ratio + apple_ratio + pineapple_ratio
    total_amount = orange_amount + apple_amount + pineapple_amount
    
    leftover_orange_amount = round(orange_amount - (orange_ratio / total_ratio) * total_amount, 6)
    leftover_apple_amount = round(apple_amount - (apple_ratio / total_ratio) * total_amount, 6)
    leftover_pineapple_amount = round(pineapple_amount - (pineapple_ratio / total_ratio) * total_amount, 6)
    
    return leftover_orange_amount, leftover_apple_amount, leftover_pineapple_amount

