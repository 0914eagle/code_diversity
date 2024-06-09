
def get_leftover_juice(amounts, ratios):
    orange_amount, apple_amount, pineapple_amount = amounts
    orange_ratio, apple_ratio, pineapple_ratio = ratios
    
    total_amount = orange_amount + apple_amount + pineapple_amount
    total_ratio = orange_ratio + apple_ratio + pineapple_ratio
    
    leftover_orange_amount = orange_amount - (total_amount * orange_ratio / total_ratio)
    leftover_apple_amount = apple_amount - (total_amount * apple_ratio / total_ratio)
    leftover_pineapple_amount = pineapple_amount - (total_amount * pineapple_ratio / total_ratio)
    
    return leftover_orange_amount, leftover_apple_amount, leftover_pineapple_amount

