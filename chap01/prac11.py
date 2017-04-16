#coding: utf-8

print("Indicate the number of digits you input")
print("Number :")
num = int(input())
n = 1
i = 0
while(num - n > 0):
    n *= 10
    i += 1
print("This number has {0} digits".format(i))
