import numpy as np

def det(X):
    detX = 1
    triu_X = np.triu(X)
    for i in range(len(X)):
        detX *= X[i][i]
    return detX

def test(X):
    try:
        if len(X) == len(X[0]):
            return det(X)
        else:
            return "The given matrix is not a square matrix so doesn't have a determinant"
    except:
        return 'The given argument is not a mtrix'

def main():
    # TODO: print the determinant of given square matrix
    A = np.ones((6, 6)) * 2
    print('A = \n{}\ndet(A) = {}'.format(A, test(A)))

    # TODO: test with non-square matrix
    B = np.array([[1, 2], [2, 3], [3, 4]])
    print('B = \n{}\ndet(B) = OOPS --> {}'.format(B, test(B)))

    # TODO: test with non-array argument
    print('C = {}\ndet(C) = OOPS --> {}'.format(3, test(3)))


if __name__ == "__main__":
    main()
