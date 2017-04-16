#coding: utf-8

def ary_copy(a, b, n):
    for i in range(len(b)):
        a.append(b[i])

#Main Function(void, in C_lang)

print("Copy all elements in one array to the other.")
print("Input the number of elements that the array will have.")
n = int(input())
a = []
b = []

for i in range(n):
    print("No. {0}".format(i + 1))
    e = int(input())
    a.append(e)

ary_copy(b, a, n)
print("Copied elements from an array to the other.")

for i in range(len(b)):
    print("No.{0} : {1}".format(i + 1, b[i]))
