import numpy as np

def twoxtwo():
    #Define each entry:
    a11 = float(input("Set a11: "))
    a12 = float(input("Set a12: "))
    a21 = float(input("Set a21: "))
    a22 = float(input("Set a22: "))
    row1 = [a11, a12]
    row2 = [a21, a22]
    #Print matrix:
    print(row1)
    print(row2)
    #Run check:
    check = input("Is this your matrix? Y/N: ")
    if check == "y":
        det = (a11*a22) - (a12*a21)
        print("The determinant is: " + str(det))
    else:
        twoxtwo()

def threexthree():
    a11 = float(input("Set a11: "))
    a12 = float(input("Set a12: "))
    a13 = float(input("Set a13: "))

    a21 = float(input("Set a21: "))
    a22 = float(input("Set a22: "))
    a23 = float(input("Set a23: "))

    a31 = float(input("Set a31: "))
    a32 = float(input("Set a32: "))
    a33 = float(input("Set a33: "))

    row1 = [a11,a12,a13]
    row2 = [a21,a22,a23]
    row3 = [a31,a32,a33]

    print(row1)
    print(row2)
    print(row3)

    check = input("Is this your matrix? Y/N: ")
    if check == "y":
        det = a11*((a22*a33)-(a23*a32))-a12*((a21*a33)-(a23*a31))+a13*((a21*a32)-(a22*a31))
        print("The determinant is: " + str(det))
    else:
        threexthree()

def detmain():
    print("Select the size of your matrix:")
    choice = input("For 2x2 press 2. For 3x3 press 3: ")
    if choice == "2":
        twoxtwo()

    elif choice == "3":
        threexthree()

    else:
        detmain()
