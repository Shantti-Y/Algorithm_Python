#coding: utf-8

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
