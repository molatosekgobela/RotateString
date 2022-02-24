"""
Write a function that will rotate a array left and right
the function recieves an array and n number of times to rotate

"""
# function to rotate string left n times
def rotate_left(arry,n):

    arry_convert = []
    for i in range (len(arry)):
        arry_convert.append(arry[i])
    # Temp variable
    temp = []
    for i in range(n):
        if i < len(arry):
            temp.append(arry_convert[i])
    final = arry_convert[n:len(arry)]+temp

    #return ''.join(final)
    return final
def rotate_right(arry,n):
    
    r_first = arry[0:len(arry) - n]
    r_second = arry[len(arry) - n :]

    final = r_second+r_first

    return final
# string rotate with slicing
def rotate_left_slicing(arry,n):
    r_first = arry[:n]
    r_second = arry[n:]

    final = r_second+r_first

    return final
# driver code

if __name__== "__main__":

    arry = [1, 2, 3, 4, 5]
    #arry = 'GeeksforGeeks'
    n = 4

    print(rotate_left(arry,n))
    print(rotate_right(arry,n))
    print(rotate_left_slicing(arry,n))