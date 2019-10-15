def check():
    flag, flag2 , flag3 = 0, 0, 0
    a=input("Enter expression: ")

    s=len(a)
    if s <4:
        print("Not Accepted")
        exit()

    for i in range(s):
        if a[i] == '+' :
            index = i
            break
    for j in range(index):
        if a[j] == 'i':
            flag = 1

    x=j
    for j in range(x, s):
        if a[j] == 'i':
            flag2 = 1

    if flag == 0 and flag2 == 1:
        flag3 = 1

    if flag3 == 1:
        print("Accepted")
    else: print("Not accepted")

if __name__ == "__main__":
    check()