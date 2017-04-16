#coding: utf-8

# 整数a, bを含め、その間の全整数の和を求めて返す以下の関数を作成せよ。
# int sumof(int a, int b);
# aとbの大小関係に関係なく和を求めること。たとえばaが3でbが5であれば12を、
# aが6でbが4であれば15を求めること。


# Main function
def sumof(a, b):
    sum = 0
    if(a > b):
        temp = a
        a = b
        b = temp

    for i in range(a, b + 1):
        sum += i

    return sum

print("Calculate the sum of numbers between variables a and b")
print("Variable a:")
a = int(input())

print("Variable b:")
b = int(input())

print("Sum : {0}".format(sumof(a, b)))
