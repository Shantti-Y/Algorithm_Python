from random import randint as rand
#coding: utf-8

# List2-6(参考書参照)は身長を乱数で生成した上で身長の最大値を求めるプログラムであった。
# 身長だけでなく人数も乱数で生成するように書き換えたプログラムを作成せよ。
# 人数は、5以上20以下の乱数とすること。

def maxof(a, n):
    max = a[0]

    for i in range(n - 1):
        if(max < a[i + 1]):
            max = a[i + 1]

    return max


#Main function
print("Compare student's height among the specified number of students")
print("and determine the lowest height")

print("Number of students :")
num = rand(5, 20)
ar = []

for i in range(num):
    ar.append(rand(150, 190))

print("The max of height is {0}cm.".format(maxof(ar, num)))
