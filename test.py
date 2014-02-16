# Count the number of elements in the list l
def count_list(l):
    total = 0
    # print 'total at the top of the function is: ', total

    if l == []: # list_length == 0:
        return 0
    else:
        l.pop()
        total = count_list(l) + 1
        # print 'total is : ', total
        # print 'total', total
    return total



def reverse(l):

    length = count_list(l)
    if l[length-1]:
        return l
    else:

    # when you reach the middle, return all the reversed values

listtest = [2, 10, 'cat']
print reverse(listtest)