# Date Structure
mdays = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
]

def isleap(year):
    if((year % 4 == 0 & year % 100 != 0) | year % 400 == 0):
        return 1
    else:
        return 0

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
    year = int(n / 365)
    month = 0
    day = n % 365

    y = date.y + year

    while day >= mdays[isleap(y)][month]:
        day -= mdays[isleap(y)][month]
        month += 1
    m = date.m + month
    d = date.d + day

    if(d > mdays[0][month]):
        m += 1
        d -= mdays[0][month]
    if(m > 12):
        y += 1
        m -= 12
    return (DateOf(y, m, d))

# Return the day when n days before the day x
def Before(date, n):
    year = int(n / 365)
    month = 0
    day = n % 365

    y = date.y - year

    while day >= mdays[isleap(y)][month]:
        day -= mdays[isleap(y)][month]
        month += 1
    m = date.m - month
    d = date.d - day

    if(d <= 0):
        m -= 1
        d += mdays[0][month]
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
