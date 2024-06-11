def below_threshold(l: list, t: int):
    

    for i in l:
        if i > t:
            return False
    return True


