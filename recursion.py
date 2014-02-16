# TODO do code review
# TODO Try everything without pop

# Multiply all the elements in a list
def multiply_list(l):
    # print 'the length is :', len(l)
    total = 1

    if len(l) == 1:
        return 1
    else:
        last_var = l.pop()
        total = multiply_list(l) * last_var
        # print 'now the length is : ', len(l)
        # print 'total', total
    return total

# Return the factorial of n
def fact(n):
    if n == 1:
        return 1
    else:
       total = fact(n-1) * n
    return total

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

# Sum all of the elements in a list
def sum_list(l):
    total = 0

    if l == []: # list_length == 0:
        return 0
    else:
        var = l.pop()
        total = sum_list(l) + var
    return total

# Reverse a list without slicing or loops
def reverse(l):

# TODO What should the base case be??? see other methods of doing this with other base cases
    if l == []: 
        return []
    else:
        word = l.pop()
        reverse(l)
        l.insert(0, word)

    return l

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)

# TODO Understand this better, see drawing to understand mechanism. But in this case, really just have to trust it works
def fibonacci(n):
    if n <= 1:
        return 1
    else:         
        return fibonacci(n-1) + fibonacci(n-2)

# Finds the item i in the list l.... RECURSIVELY
# TODO check that i is an index, CHECK if I am doing this correctly? base case return or pass both work? 
#   Why can't I just put it in the base case return (if base case: return l[i]) - returns None?
def find(l, i):
    # print "this is the list at the top of the chart: ", l
    if len(l) == i+1:
        pass #TODO or return alone works too
        # print "you are awesome!"
        # TODO why doesn't it work just to have the return statement from down below here? 
            # Because it disappears when the function is run again, when it goes backwards
    else: 
        new_item = l.pop()
        # print "this is what was popped off: ", new_item         
        find(l, i)

    return l[i] # TODO, this could go above too, it will keep running backwards and capture the last time? 

# Determines if a string is a palindrome
def palindrome(some_string):
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    return (0, 0)

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return