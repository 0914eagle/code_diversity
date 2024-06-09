
def get_leftover_juice(amounts, ratios):
    orange_amount, apple_amount, pineapple_amount = amounts
    orange_ratio, apple_ratio, pineapple_ratio = ratios
    
    total_ratio = orange_ratio + apple_ratio + pineapple_ratio
    orange_needed = orange_ratio / total_ratio * 100
    apple_needed = apple_ratio / total_ratio * 100
    pineapple_needed = pineapple_ratio / total_ratio * 100
    
    orange_leftover = orange_amount - orange_needed
    apple_leftover = apple_amount - apple_needed
    pineapple_leftover = pineapple_amount - pineapple_needed
    
    return orange_leftover, apple_leftover, pineapple_leftover

