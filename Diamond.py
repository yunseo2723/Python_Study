#s = input("문자 하나 입력 : ")
s='@'
for k in range(0,9,1):
    if k < 5 :
        for i in range(0, 4 - k, 1):
            print(" ", end="")
        for i in range(0, k * 2 + 1, 1):
            print("%s" % s, end="")
        print()
    else :
        for i in range(0, k - 4, 1):
            print(" ", end="")
        for i in range(0, 2 * ( 9 - k ) - 1, 1):
            print("%s" % s, end="")
        print()
