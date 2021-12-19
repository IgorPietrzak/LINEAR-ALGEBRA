import numpy as np

def eigenvalues():
    print("Matrix format: a b c;d e f;g h i")
    matrix = input("Enter matrix in the above format: ")
    print(matrix)
    mat = np.mat(matrix)
    print(mat)
    sure = input("Is this your matrix? Y/N: ")
    if sure == 'y':

        print("")
        evalue, evect = np.linalg.eig(mat)


        print("eigenvalues: \n")
        print(evalue)
        print("~~~~~~~~~~~~~~~~~~~~~~\n")
    else:
        eigenvalues()
