#coding: utf-8

print("Display the number depending on you input of asterisks")

print("Height :")
h = int(input())
print("Width :")
w = int(input())

for i in range(h):
    a = []
    for j in range(w):
        a.append("*")
    a = "".join(a)
    print(a)
