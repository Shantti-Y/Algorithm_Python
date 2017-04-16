#coding: utf-8

def card_convr(x, n, d):
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if(x == 0):
        d.insert(0, dchar[0])
        print("     |\t0")
    else:
        while(x):
            print("  {0}|\t{1}\t...{2}".format(str(n).ljust(3), x, x % n))
            print("     +----------")
            d.insert(0, dchar[x % n])
            x = int(x / n)
        print("     |\t0")

#Main function
print("Convert Decimal num in redix convertive method")

y = 1
while(y == 1):

    print("Number that should be converted :")
    num = int(input())
    red = 100
    while(red < 2 | red > 36):
        print("What kind of number do you want to convert from decimal num?")
        red = int(input())
    cno = []
    card_convr(num, red, cno)

    print("Decimal Number {0} has :".format(red))
    cno = "".join(cno)
    print(cno)
    print("Do you want to re-activate this program? (1..Yes / 0..No)")
    y = int(input())
