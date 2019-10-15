def finish():
    print("Not Accepted!")
    exit()

def check():
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
if __name__ == "__main__":
    check()