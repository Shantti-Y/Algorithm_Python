# coding: utf-8

# 九九の掛け算ではなく足し算を行う表を表示するプログラムを作成せよ。
# 前問と同様に、表の上と左に足す数を表示すること。


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
        n = i + j
        a.append(str(n).rjust(3))

    a = " ".join(a)
    print(" {0} |{1}".format(i, a))
