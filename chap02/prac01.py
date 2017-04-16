#coding: utf-8

def minof(a, n):
    lowest = a[0]

    for i in range(n - 1):
        if(lowest > a[i + 1]):
            lowest = a[i + 1]
    return lowest

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

print("The lowest height is {0}cm.".format(minof(ar, num)))
