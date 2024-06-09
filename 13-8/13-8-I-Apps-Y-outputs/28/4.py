
def find_midpoint(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    total_minutes = (h2 - h1) * 60 + (m2 - m1)
    midpoint_minutes = total_minutes // 2
    h3 = midpoint_minutes // 60
    m3 = midpoint_minutes % 60
    return f"{h3:02d}:{m3:02d}"

