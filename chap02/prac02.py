#coding: utf-8

def sumof(a, n):
    sum = 0

    for i in range(n):
        sum += a[i]
    return sum

#Main function
print("Compare student's height among the specified number of students")
print("and determine the lowest height")

print("Number of students :")
num = int(input())
ar = []

print("Input each height")
for i in range(num):
    print("Student No.{0} : ".format(i + 1))
    ar.append(int(input()))

print("The sum of height is {0}cm.".format(sumof(ar, num)))
