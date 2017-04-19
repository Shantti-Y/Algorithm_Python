#coding: utf-8

# List2-8(参考書参照)の関数card_convrを書き換えて、配列の先頭側に下位桁ではなく
# 上位桁を格納する関数card_convを作成せよ。
# int card_conv(unsigned x, int n, char d[]);

def card_convr(x, n, d):
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = 0

    if(x == 0):
        d.append(dchar[0])
    else:
        while(x):
            d.append(dchar[x % n])
            x = int(x / n)
            digits += 1
    return digits


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
    dno = card_convr(num, red, cno)

    print("Decimal Number {0} has :".format(dno))
    cno = "".join(cno)
    print(cno)
    print("Do you want to re-activate this program? (1..Yes / 0..No)")
    y = int(input())
