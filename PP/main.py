from det import detmain,twoxtwo,threexthree
from evals import eigenvalues

def main():
    print("Press E for eigenvalue calculator.")
    print("Press D for determinant calculator.")
    pick = input("Choose: ")
    if pick == "d":
        detmain()
    elif pick == "e":
        eigenvalues()
    else:
        print("Invalid input, try again.")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        main()
main()
end = True
while end == True:
    cont = input("Would you like to re-run the program? Y/N: ")
    if cont == "y":
        main()  
    elif cont == "n":
        exit()
