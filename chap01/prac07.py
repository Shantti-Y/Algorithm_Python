# coding: utf-8

# List1-5(参考書参照)のプログラムをもとにして、たとえばnが7であれば、『1から7までの和は28です。』と
# 表示するのではなく、『1 + 2 + 3 + 4 + 5 + 6 + 7 = 28』と表示するプログラムを作成せよ。


# Main function
print("Calculate a sum of numbers from 1 to n variable.")
print ("Variable n : ")
n = int(input())

sum = 0
st = []

for i in range(1, n + 1):
    sum += i
    st.append(str(i))

st = " + ".join(st)

print("{0} = {1}".format(st, sum))
