def password():
    flag, flag1, flag2, flag3 = 0 , 0 , 0, 0
    a = input("Enter password: ")
    temp = 1
    b = len(a)
    if len(a)<8:
        temp = 0

    for i in range(len(a)):
        if a[i]>='A' and a[i] <= 'Z':
            flag=1
        if a[i] >= 'a' and a[i] <= 'z':
            flag1=1
        if a[i] >= '0' and a[i] <= '9':
            flag2=1
    if a[b-1] == '@' or a[b-1] == '#' or a[b-1] == '$' or a[b-1] == '&':
            flag3=1
    if flag == 1 and flag1 == 1 and flag2 == 1 and temp ==1 and flag3 ==1:
        print("Accepted")
    else:
        print("Not accepted")

if __name__ == "__main__":
    password()
