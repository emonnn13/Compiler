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

if __name__ == "__main__":
    r_id()
