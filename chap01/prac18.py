# coding: utf-8

# 下を向いたn段の数字ピラミッドを表示する関数を作成せよ。
# void nrpira(int n);
# 第i行目に表示する数字は、i % 10によって求めること

def nrpira(n):
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

# Main Function
print("Display the isosceles triangle which side length depends on you input")
print("Length :")
n = int(input())

print("Triangle")
nrpira(n)
