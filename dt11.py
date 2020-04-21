import datetime

date1 = datetime.date(2019, 12, 25)
date2 = datetime.date(2019, 12, 31)

difference = date2 - date1
f_difference = difference.total_seconds()
m_difference = f_difference // 60

print(m_difference, "min")
