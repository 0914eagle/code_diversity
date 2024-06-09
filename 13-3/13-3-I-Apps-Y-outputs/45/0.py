
def get_leftover_juice(amounts, ratios):
    orange_amount, apple_amount, pineapple_amount = amounts
    orange_ratio, apple_ratio, pineapple_ratio = ratios
    
    total_amount = orange_amount + apple_amount + pineapple_amount
    total_ratio = orange_ratio + apple_ratio + pineapple_ratio
    
    leftover_orange_amount = orange_amount - (orange_ratio / total_ratio) * total_amount
    leftover_apple_amount = apple_amount - (apple_ratio / total_ratio) * total_amount
    leftover_pineapple_amount = pineapple_amount - (pineapple_ratio / total_ratio) * total_amount
    
    return leftover_orange_amount, leftover_apple_amount, leftover_pineapple_amount

