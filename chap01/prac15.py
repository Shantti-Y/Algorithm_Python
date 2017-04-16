# coding: utf-8

# 読み込んだ高さと横幅をもつ長方形を*記号で表示するプログラムを作成せよ。


# Main function
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
