#coding: utf-8

#Isosceles triangle shaped with right angle at the left bottom
def spira(n):
    i = n
    while(i > 0):
        l = (i - 1) * 2 + 1
        a = []
        for j in range(n - i):
            a.append(" ")
        for k in range(l):
            a.append(str(n - i + 1))
        a = "".join(a)
        print(a)
        i -= 1

print("Display the isosceles triangle which side length depends on you input")
print("Length :")
n = int(input())

print("Triangle at the left bottom")
spira(n)
