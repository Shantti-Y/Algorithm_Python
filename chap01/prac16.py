# coding: utf-8

# 直角二等辺三角形を表示する部分を独立させて、以下の形式の関数として実現せよ。
# void triangleLB(int n)    /* 左下側が直角の二等辺三角形を表示 */
# さらに、直角が左上側、右上側、右下側の二等辺三角形を表示する関数を作成せよ。
# void triangleLU(int n)    /* 左上側が直角の二等辺三角形を表示 */
# void triangleRU(int n)    /* 右上側が直角の二等辺三角形を表示 */
# void triangleRB(int n)    /* 右下側が直角の二等辺三角形を表示 */


#Isosceles triangle shaped with right angle at the left bottom
def triangleLB(n):
    k = 1
    for i in range(n):
        a = []
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k += 1

#Isosceles triangle shaped with right angle at the left top
def triangleLU(n):
    k = n
    for i in range(n):
        a = []
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k -= 1

#Isosceles triangle shaped with right angle at the right top
def triangleRU(n):
    k = n
    for i in range(n):
        a = []
        for j in range(n - k):
            a.append(" ")
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k -= 1

#Isosceles triangle shaped with right angle at the right bottom
def triangleRB(n):
    k = 1
    for i in range(n):
        a = []
        for j in range(n - k):
            a.append(" ")
        for j in range(k):
            a.append("*")
        a = "".join(a)
        print(a)
        k += 1


# Main function
print("Display the isosceles triangle which side length depends on you input")
print("Length :")
n = int(input())

print("Triangle at the left bottom")
triangleLB(n)

print("Triangle at the left top")
triangleLU(n)

print("Triangle at the right top")
triangleRU(n)

print("Triangle at the right bottom")
triangleRB(n)
