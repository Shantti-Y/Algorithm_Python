#coding: utf-8

#Isosceles triangle shaped with right angle at the left bottom
def triangleLB(n):
    k = 1
    for i in range(n):
        a = []
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k += 1

#Isosceles triangle shaped with right angle at the left top
def triangleLU(n):
    k = n
    for i in range(n):
        a = []
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k -= 1

#Isosceles triangle shaped with right angle at the right top
def triangleRU(n):
    k = n
    for i in range(n):
        a = []
        for j in range(n - k):
            a.append(" ")
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k -= 1

#Isosceles triangle shaped with right angle at the right bottom
def triangleRB(n):
    k = 1
    for i in range(n):
        a = []
        for j in range(n - k):
            a.append(" ")
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k += 1

print("Display the isosceles triangle which side length depends on you input")
print("Length :")
n = int(input())

print("Triangle at the left bottom")
triangleLB(n)

print("Triangle at the left top")
triangleLU(n)

print("Triangle at the right top")
triangleRU(n)

print("Triangle at the right bottom")
triangleRB(n)
