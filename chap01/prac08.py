#　coding: utf-8

# たとえば、1から10までの和は(1 + 10) * 5によって求められる。ガウスの方法と呼ばれる、
# この方法を用いて、1からnまでの整数の和を求めるプログラムを作成せよ。


# Main function
print("Calculate the sum of numbers from 1 to the variable n in Gauss's law ")
print("Variable n : ")
n = float(input())

sum = int((1 + n) * (n / 2))

print("The sum = {0}".format(sum))
