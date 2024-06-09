
def get_leftover_juice(amounts, ratios):
    orange_amount, apple_amount, pineapple_amount = amounts
    orange_ratio, apple_ratio, pineapple_ratio = ratios
    
    total_ratio = orange_ratio + apple_ratio + pineapple_ratio
    orange_leftover = orange_amount - (orange_amount * orange_ratio / total_ratio)
    apple_leftover = apple_amount - (apple_amount * apple_ratio / total_ratio)
    pineapple_leftover = pineapple_amount - (pineapple_amount * pineapple_ratio / total_ratio)
    
    return orange_leftover, apple_leftover, pineapple_leftover

