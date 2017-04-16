#coding: utf-8

print("Display the number depending on you input of asterisks")
print("Stages :")
n = int(input())

for i in range(n):
    a = []
    for j in range(n):
        a.append("*")
    a = "".join(a)
    print(a)
