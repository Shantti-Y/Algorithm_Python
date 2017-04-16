#coding: utf-8

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
