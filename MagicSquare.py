#  File: MagicSquare.py

#  Description: Magic Square Algorithm

#  Date Created: 10/19/2020

#  Date Last Modified: 10/19/2020


from math import sqrt

# checks if a 1-D list if converted to a 2-D list is magic
# a is 1-D list of integers
# returns True if a is magic and False otherwise
def is_magic ( a ):
    # length = n,  magicConstant = (n * (n^2 + 1) / 2)
    length = int(sqrt(len(a)))
    magicConstant = int(length * (length**2 + 1) / 2)

    # create a 2d list (matrix)
    matrix = [a[i:i+length] for i in range(0, len(a), length)]
    
    # horizontal and vertical search (row, column)
    for row in range(len(matrix)):
        # horizontal sum (row)
        if sum(matrix[row]) != magicConstant:
            return False
        # vertical sum (column)
        elif sum(a[row::length]) != magicConstant:
            return False
    
    # diagonal search
    diag1 = 0
    diag2 = 0
    for i in range(length):
        diag1 += matrix[i][i]
        diag2 += matrix[i][length-i-1]
    if (diag1 != magicConstant) or (diag2 != magicConstant):
        return False

    return True


# this function recursively permutes all magic squares
# a is 1-D list of integers and idx is an index in a
# it stores all 1-D lists that are magic in the list all_magic
def permute ( a, idx, all_magic ):
    hi = len(a)
    if idx == hi and is_magic(a):
        all_magic.append(a[:])
    else:
        n = int(sqrt(hi))
        for i in range(idx, hi):
            a[idx], a[i] = a[i], a[idx]
            if (idx + 1) % n == 0:
                magic =  n * (n ** 2 + 1) / 2
                if (sum(a[idx + 1 - n:idx]) < magic - n ** 2) or (magic <= sum(a[idx + 1 - n:idx])):
                    break
            permute(a, idx + 1, all_magic)
            a[idx], a[i] = a[i], a[idx]


def main():
    # read the dimension of the magic square
    in_file = open ('magic.in', 'r')
    line = in_file.readline()
    line = line.strip()
    n = int (line)
    in_file.close()

    # create an empty list for all magic squares
    all_magic = []

    # create the 1-D list that has the numbers 1 through n^2
    a = [i for i in range(1, n**2 + 1)]
    
    # generate all magic squares using permutation 
    permute(a, 0, all_magic)

    # print all magic squares
    #print(all_magic)
    
    for s in all_magic:
        print(s)


if __name__ == "__main__":
    main()
