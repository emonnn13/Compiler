def main():
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


if __name__ == "__main__":
    main()