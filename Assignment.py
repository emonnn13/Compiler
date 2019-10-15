def r_id():

    flag = 0

    x = input("Enter ID: ")

    if len(x) != 9 or x[6:9] == '000':
        print("Not accepted")
        exit()

    if x[0:3] == '011':
        if x[5] == '3' or x[5] == '1' or x[5] == '2':
            if (x[6] >= '0' and x[6] <= '9') or (x[7] >= '0' and x[7] <= '9') or x[8] >= '0' and x[8] <= '9':
                print("Accepted")
                exit()
            else: flag = 0
        else: flag =0
    else: flag = 0
    if flag == 0:
        print("Not accepted")


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


def finish():
    print("Not Accepted!")
    exit()

def st_check():
    flag = 0
    x = input("Enter: ")
    if len(x)<3 :
       finish()
    if x[0] >= '0' or x[0] <= 9:
        if x[1].isupper() :
            if not x[2].isalpha():
                flag = 1
            else:
                flag = 0
        else:
            flag = 0
    else:
        flag = 0

    if flag == 1:
        print("Accepted.")
    else:
        print("Not Accepted.")

def nm_check():
    flag , z = 1 , 1

    number = input("Enter a no: ")
    x= len(number)
    if number[x-1] == '.':
        print("Not accepted")
        exit()
    for i in range (x):
        if (number[i] >= 'A' and number[i] <= 'Z') or (number[i] >= 'a' and number[i] <= 'z'):
            flag = 0
        elif number[i] == '.':
            if number[i+1]>= '0' and number[i+1]<= '9':
                z=0
            else:
                z=5
    if flag == 0 : print("Not accepted.")
    elif z==0 : print("Accepted")
    elif z==5 : print("Not accepted")
    else: print("Accepted")

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
    while True:
        print('''
        ENTER 1 TO CHECK UIU CSE ID: 
        ENTER 2 TO CHECK COMPLEX NUMBER: 
        ENTER 3 TO CHECK RE WHICH ACCEPT A SPECIFIC CRITERIA: 
        ENTER 4 TO CHECK RE TO THAT CONTAIN BOTH INTEGER AND FLOATING POINT: 
        ENTER 5 TO CHECK A SPECIFIC PASSWORD CRITERIA: 
        ENTER 6 TO EXIT.
        ''')
        a = int(input("Enter choice:"))
        if a == 1:
            r_id()
        elif a == 2:
            check()
        elif a == 3:
            st_check()
        elif a == 4:
            nm_check()
        elif a == 5:
            password()
        elif a == 6:
            exit()
