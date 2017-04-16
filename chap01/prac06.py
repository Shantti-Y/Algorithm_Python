# coding: utf-8

# List1-4(参考書参照)のwhile文終了時点における変数iの値がi + 1となることを確認せよ
# (変数iの値を表示するように書き換えたプログラムを作成すること)


# Main function
print("Calculate a sum of numbers ftom 1 to n variable.")
print ("Variable n : ")
n = int(input())

sum = 0
i = 1
while(i <= n):
    sum += i
    i += 1

print("Total: {0}".format(sum))
print("Number of iterated times: {0}".format(i))
