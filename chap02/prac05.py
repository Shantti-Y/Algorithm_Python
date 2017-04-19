#coding: utf-8

# 配列要素の並びの反転の経過を逐一表示するようにList2-7(参考書参照)を書き換えたプログラムを
# 作成せよ。(関数ary_reverseに手を加えること)。

def ary_reverse(a, n):
    for i in range(int(n / 2)):
        temp = a[i]
        a[i] = a[n - i - 1]
        a[n - i - 1] = temp
        print("{0}".format(a))
        print("a[{0}]とa[{1}]を交換します。".format(i, (n - i - 1)))
        

#Main function
print("Compare student's height among the specified number of students")
print("and determine the lowest height")

print("Number of students :")
num = int(input())
ar = []

for i in range(num):
    print("No.{0}:".format(i + 1))
    ar.append(int(input()))

print("Before: {0}".format(ar))
ary_reverse(ar, num)
print("After : {0}".format(ar))
