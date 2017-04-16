# coding: utf-8

# 読み込んだ段数を一辺としてもつ正方形を*記号で表示するプログラムを作成せよ。


# Main function
print("Display the number depending on you input of asterisks")
print("Stages :")
n = int(input())

for i in range(n):
    a = []
    for j in range(n):
        a.append("*")
    a = "".join(a)
    print(a)
