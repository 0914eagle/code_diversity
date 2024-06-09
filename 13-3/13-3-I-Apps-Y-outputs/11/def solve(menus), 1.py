
def solve(menus):
    for menu in menus:
        if "pea soup" in menu and "pancakes" in menu:
            return menu[0]
    return "Anywhere is fine I guess"

