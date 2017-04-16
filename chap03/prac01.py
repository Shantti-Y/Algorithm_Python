# Linear Search (in a sentinel law)

def search(a, n, key):
    a.append(key)
    for i in range(n + 1):
        if(a[i] == key):
            break

    return -1 if i == n else i


# Main Function(void)

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
