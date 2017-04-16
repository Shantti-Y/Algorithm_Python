# Linear Search (Standardized way)

def search(a, n, key):
    st_num = []
    st_ele = []
    for i in range(n):
        st_num.append(str("{0}".format(i)))
        st_ele.append(str("{0:02d}".format(a[i])))
    st_num = "   ".join(st_num)
    st_ele = "  ".join(st_ele)

    print("   |    {0}".format(st_num))
    print("---+--{0}".format("----" * n))
    for i in range(n):
        print("   |    {0}{1}{2}".format(("    " * i), "*", ("    " * (n - i))))
        print("  {0}|   {1}".format(i, st_ele))
        if(a[i] == key):
            return i

    return -1


# Main Function

print("I'm gonna search a key you input in a linear method with a sentiel law")
print("Number of elements :")
nx = int(input())
ar = []

for i in range(nx):
    print("x[{0}] :".format(i))
    x = int(input())
    ar.append(x)

print("The key :")
ky = int(input())

idx = search(ar, nx, ky)

if(idx == -1):
    print("Failed searching {0}".format(ky))
else:
    print("{0} is in x[{1}]".format(ky, idx))
