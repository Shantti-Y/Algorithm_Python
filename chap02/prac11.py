#coding: utf-8

# 関数dayofyearを、変数iとdaysを使わずに実現するように書き換えよ。while文を使うこと。

mdays = [
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
]

#Confirm whether input year is a leap year
def isleap(year):
    if((year % 4 == 0 & year % 100 != 0) | year % 400 == 0):
        return 1
    else:
        return 0

def dayofyear(y, m, d):
    m -= 1
    while m > 0:
        d += mdays[isleap(y)][m - 1]
        m -= 1

    return d


#Main Function
retry = 1

while(retry == 1):
    print("Year:")
    year = int(input())
    print("Month:")
    month = int(input())
    print("Day")
    day = int(input())

    print("{0} days has passed in this year".format(dayofyear(year, month, day)))

    print("Do you want to do again? (1)...Yes (2)...No")
    retry = int(input())
