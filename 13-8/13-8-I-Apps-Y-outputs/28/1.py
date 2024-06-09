
def get_midpoint(time1, time2):
    h1, m1 = map(int, time1.split(':'))
    h2, m2 = map(int, time2.split(':'))
    m_total = (h2 - h1) * 60 + (m2 - m1)
    m_mid = m_total // 2
    h_mid = h1 + m_mid // 60
    m_mid = m_mid % 60
    return f"{h_mid:02d}:{m_mid:02d}"

