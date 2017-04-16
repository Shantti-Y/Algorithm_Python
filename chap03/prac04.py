# Binary Search
def bin_search(a, n, key):

    st_num = []
    st_ele = []
    for i in range(n):
        st_num.append(str("{0}".format(i)))
        st_ele.append(str("{0:02d}".format(a[i])))
    st_num = "   ".join(st_num)
    st_ele = "  ".join(st_ele)

    print("   |    {0}".format(st_num))
    print("---+--{0}".format("----" * n))

    pl = 0
    pr = n - 1

    while(pl <= pr):
        pc = int((pl + pr) / 2)

        # Creating binary search syntax
        b_str = []
        for i in range(n):
            if(i == pl):
                b_str.append("<-  ")
            elif(i == pc):
                b_str.append(" +  ")
            elif(i == pr):
                b_str.append("->  ")
            else:
                b_str.append("    ")
        b_str = "".join(b_str)
        print("   |   {0}".format(b_str))
        print("  {0}|   {1}".format(pc, st_ele))

        if(a[pc] == key):
            return pc
        elif(a[pc] < key):
            pl = pc + 1
        else:
            pr = pc - 1

    return -1


# Main Function
print("I'm gonna search a key you input in a binary method")
print("Number of elements :")
nx = int(input())
ar = []

for i in range(nx):
    while(True):
        print("x[{0}] :".format(i))
        x = int(input())
        if(i == 0 or x > ar[i - 1]):
            ar.append(x)
            break

print("The key :")
ky = int(input())

idx = bin_search(ar, nx, ky)

if(idx == -1):
    print("Failed Searching '{0}'".format(ky))
else:
    print("{0} is in x[{1}]".format(ky, idx))
