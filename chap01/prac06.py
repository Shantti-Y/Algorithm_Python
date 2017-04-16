#coding: utf-8

print("Calculate a sum of numbers ftom 1 to n variable.")
print ("Variable n : ")
n = int(input())

sum = 0
i = 1
while(i <= n):
    sum += i
    i += 1


print("Total: {0}".format(sum))
print("Number of iterated times: {0}".format(i))
