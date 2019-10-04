def main():
    flag = 0
    number = input("Enter a no: ")

    if number[0] == '+' or number[0] == '-':
        flag = 1
    if number.isnumeric() and flag == 1 : #isnumercic calls false -> else.
         print("Accepted")
    else:
        print("Not Accepted.")


if __name__ == "__main__":
    main()