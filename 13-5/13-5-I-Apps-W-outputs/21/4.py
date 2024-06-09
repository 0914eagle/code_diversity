
def weightlifting_walrus(plates):
    plates.sort(reverse=True)
    total = 0
    for plate in plates:
        total += plate
        if total >= 1000:
            break
    if total < 1000:
        return total + plates[0]
    else:
        return total

