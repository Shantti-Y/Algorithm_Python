# coding: utf-8

# 二つの変数a, bに整数値を読み込んでb - aの値を表示するプログラムを作成せよ。
# なお、変数bに読み込んだ値がa以下であれば、変数bの値を再入力させること。


# Main function
print("Calculate the diff of numbers in variables a and b")

i = 0
diff = 0
while(i == 0):

    print("Variable a:")
    a = int(input())

    print("Variable b:")
    b = int(input())

    if(b < a):
        print("Please input the larger number into b than a")
        continue

    i += 1

diff = b - a

print("Diff : {0}".format(diff))
