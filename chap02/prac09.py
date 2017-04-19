#coding: utf-8

# 配列bの全要素を配列aに逆順にコピーする関数を作成せよ(nは要素数である)。
# void ary_rcopy(int a[], const int b[], int n);

def ary_rcopy(a, b, n):
    for i in range(len(b)):
        a.insert(0, b[i])


#Main Function

print("Copy all elements in one array to the other.")
print("Input the number of elements that the array will have.")
n = int(input())
a = []
b = []

for i in range(n):
    print("No. {0}".format(i + 1))
    e = int(input())
    a.append(e)

ary_rcopy(b, a, n)
print("Copied elements from an array to the other.")

for i in range(len(b)):
    print("No.{0} : {1}".format(i + 1, b[i]))
