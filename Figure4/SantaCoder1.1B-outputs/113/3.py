def odd_count(lst):
    
    odd_count = []
    for i in lst:
        odd_count.append(len(re.findall(r'\d+', i)))
    return odd_count


