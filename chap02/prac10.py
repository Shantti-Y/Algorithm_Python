import random as rand

#coding: utf-8

# 配列aの全要素の並びをシャッフルする(無作為な順に並べる)関数を作成せよ(nは要素数である)。
# void shuffle(int a[], int n);

def shuffle(a, n):
    # 2 ways to shuffle elements in one array
    b = []

    while(len(b) < len(a)):
        bool = 0
        r = rand.randint(0, n - 1)
        for i in range(len(b)):
            if(b[i] == a[r]):
                bool = 1
                break

        if(bool == 0):
            b.append(a[r])


#Main Function

print("Copy all elements in one array to the other.")
print("Input the number of elements that the array will have.")
n = int(input())
a = []

for i in range(n):
    print("No. {0}".format(i + 1))
    e = int(input())
    a.append(e)

a = shuffle(a, n)
print("Shuffled elements from an array")

for i in range(len(a)):
    print("No.{0} : {1}".format(i + 1, a[i]))
