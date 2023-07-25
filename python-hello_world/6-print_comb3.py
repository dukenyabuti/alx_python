for i in range(0, 9):
    for j in range(i+1, 10):
        if i == 0:
            print("{:d}{:d}".format(i, j), end=", ")
        else:
            print("{:02d}".format(int(str(i)+str(j))), end=", ")
print()