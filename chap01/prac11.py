# coding: utf-8

# 正の整数値を読み込んで、その値の桁数を表示するプログラムを作成せよ。
# たとえば、135を読み込んだら『その数は3桁です。』と表示し、1314を読み込んだら『その数は4桁です。』と表示すること。


# Main function
print("Indicate the number of digits you input")
print("Number :")
num = int(input())
n = 1
i = 0
while(num - n > 0):
    n *= 10
    i += 1
print("This number has {0} digits".format(i))
