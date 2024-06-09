
def get_leftover_juice(juice_amounts, juice_ratios):
    orange_amount, apple_amount, pineapple_amount = juice_amounts
    orange_ratio, apple_ratio, pineapple_ratio = juice_ratios
    
    total_juice_amount = orange_amount + apple_amount + pineapple_amount
    total_juice_ratio = orange_ratio + apple_ratio + pineapple_ratio
    
    leftover_orange_amount = orange_amount - (orange_ratio / total_juice_ratio) * total_juice_amount
    leftover_apple_amount = apple_amount - (apple_ratio / total_juice_ratio) * total_juice_amount
    leftover_pineapple_amount = pineapple_amount - (pineapple_ratio / total_juice_ratio) * total_juice_amount
    
    return leftover_orange_amount, leftover_apple_amount, leftover_pineapple_amount

