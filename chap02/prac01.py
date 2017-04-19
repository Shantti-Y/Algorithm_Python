#coding: utf-8

# List2-5(参考書参照)は、身長の最大値を求めるプログラムであった。最小値を求めるように
# 書き換えたプログラムを作成せよ。最小値を求める手続きは、以下の形式の関数として実現する事
# int minof(const int a[], int n);

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
