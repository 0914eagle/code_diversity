
def is_takahashi_on_time(d, t, s):
    time_to_reach_place = d / s
    if time_to_reach_place <= t:
        return "Yes"
    else:
        return "No"

