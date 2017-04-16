# Date Structure


class Date(object):

    def __init__(self, y, m, d):
        if not isinstance(y, int):
            raise TypeError("y must be set to a integer")
        if not isinstance(m, int):
            raise TypeError("m must be set to a integer")
        if not isinstance(d, int):
            raise TypeError("d must be set to a integer")
        self.y = y
        self.m = m
        self.d = d

# Express Date class as "y年m月d日"
def DateOf(y, m, d):
    return "{0}年{1:02d}月{2:02d}日".format(y, m, d)

# Return the day when n days after the day x
def After(date, n):
    years = n
    y = date.y + (int(years / 365))
    months = years % 365
    m = date.m + (int(months / 31))
    days   = months % 31
    d = date.d + (int(days))
    if(d > 31):
        m += 1
        d -= 31
    if(m > 12):
        y += 1
        m -= 12
    return (DateOf(y, m, d))

# Return the day when n days before the day x
def Before(date, n):
    years = n
    y = date.y - (int(years / 365))
    months = years % 365
    m = date.m - (int(months / 31))
    days   = months % 31
    d = date.d - (int(days))
    if(d <= 0):
        m -= 1
        d += 31
    if(m <= 0):
        y -= 1
        m += 12
    return (DateOf(y, m, d))

# Main function
dates = [
    Date(1992, 8,  25),
    Date(2017, 4,  12),
    Date(2001, 1,   1),
    Date(1999, 12, 31)
]

print("--- These date list ---")
print("Year        Month   Day")
for elem in dates:
    print("{0}          {1:02d}     {2:02d}".format(elem.y, elem.m, elem.d))

print("The following shows dates in a speified format")
for elem in dates:
    print(DateOf(elem.y, elem.m, elem.d))

print("The following shows dates after specified days, please input the days you want")
d_after = int(input())
for elem in dates:
    print(After(elem, d_after))

print("The following shows dates before specified days, please input the days you want")
d_before = int(input())
for elem in dates:
    print(Before(elem, d_before))
