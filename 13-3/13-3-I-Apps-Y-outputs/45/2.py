
def get_leftover_amounts(bought, recipe):
    orange_bought, apple_bought, pineapple_bought = bought
    orange_ratio, apple_ratio, pineapple_ratio = recipe
    
    total_juice = orange_bought + apple_bought + pineapple_bought
    total_ratio = orange_ratio + apple_ratio + pineapple_ratio
    
    cocktail_amount = total_juice * (total_ratio / 100)
    
    orange_leftover = orange_bought - (cocktail_amount * (orange_ratio / total_ratio))
    apple_leftover = apple_bought - (cocktail_amount * (apple_ratio / total_ratio))
    pineapple_leftover = pineapple_bought - (cocktail_amount * (pineapple_ratio / total_ratio))
    
    return orange_leftover, apple_leftover, pineapple_leftover

