#coding: utf-8

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
