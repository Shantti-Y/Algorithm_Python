# coding: utf-8

# n段のピラミッドを表示する関数を作成せよ。
# void spira(int, n);
# 第i行目には(i - 1) * 2 + 1個の記号文字'*'を表示すること
# (そのため、最終行の第n行目には(n - 1) * 2 + 1を表示することになる。)


#Isosceles triangle shaped with right angle at the left bottom
def spira(n):
    for i in range(1, n + 1):
        l = (i - 1) * 2 + 1
        a = []
        for j in range(n - i):
            a.append(" ")
        for k in range(l):
            a.append("*")
        a = "".join(a)
        print(a)

# Main Function
print("Display the isosceles triangle which side length depends on you input")
print("Length :")
n = int(input())

print("Triangle at the left bottom")
spira(n)
