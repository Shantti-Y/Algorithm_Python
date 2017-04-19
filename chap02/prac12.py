# coding: utf-8

# List2-13(参考書参照)のプログラムの視力の分布の表示を、グラフのような形で出力するように
# 書き換えたプログラムを作成せよ。記号文字'*'を人数分だけ繰り返し表示する事。

# The array about a structure of physical examination datas
VMAX = 21

# The physical examination data
class PhysCheck(object):

    def __init__(self, name, height, vision):
        if not isinstance(name, str):
            raise TypeError("name must be set to a string")
        if not isinstance(height, int):
            raise TypeError("height must be set to an integer")
        if not isinstance(vision, float):
            raise TypeError("vision must be set to a float")
        self.name = name
        self.height = height
        self.vision = vision

# Calculate the height average
def ave_height(dat):
    sum = float(0)

    for elem in dat:
        sum += elem.height

    return sum / len(dat)

# Estimate the vision distribution
def dist_vision(dat, dist):

    for elem in dat:
        if elem.vision >= 0.0 and elem.vision <= (VMAX / 10.0):
            dist[int(elem.vision * 10)] += 1


# Main function
x = [
    PhysCheck("AKASAKA Tadao",      162, 0.3),
    PhysCheck("KATOH Tomiaki",      173, 0.7),
    PhysCheck("SAITOH Syouji",      175, 0.7),
    PhysCheck("TAKEDA Shinya",      171, 0.7),
    PhysCheck("NAGAHAMA Masaki",    168, 0.3),
    PhysCheck("HAMADA Tetsuaki",    174, 0.7),
    PhysCheck("MATSUTOMI Akio",     169, 0.8)
]

vdist = [0] * VMAX

print("■□■ Physical Examination List ■□■")
print(" name              Height  Vision")
print("---------------------------------")

for elem in x:
    print("{0}\t     {1}     {2}".format(elem.name, elem.height, elem.vision))

print("Height Average : {0:.1f}cm".format(ave_height(x)))

dist_vision(x, vdist)

for i in range(VMAX):
    plus = []
    for j in range(vdist[i]):
        plus.append("+")
    plus = "".join(plus)
    print("{0:3.1f}～：{1}".format(i / 10, plus))
