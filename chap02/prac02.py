#coding: utf-8

# 前問を書き換えて、身長の合計値を求めるプログラムを作成せよ。合計値を求める手続きは、
# 以下の形式の関数として実現する事。
# int sumof(const int a[], int n);

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
