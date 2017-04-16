# coding: utf-8

# 上と左に掛ける数がついた九九の表を表示するプログラムを作成せよ。
# 表示には、縦線記号文字'|'、マイナス記号文字'-'、プラス記号文字'+'を用いること。


# Main function
head = []
for i in range(1, 10):

    head.append(str(i).rjust(3))

head = " ".join(head)
print("   |{0}".format(head))
print("---------------------------------------")

for i in range(1, 10):
    a = []
    for j in range(1, 10):
        n = i * j
        a.append(str(n).rjust(3))

    a = " ".join(a)
    print(" {0} |{1}".format(i, a))
