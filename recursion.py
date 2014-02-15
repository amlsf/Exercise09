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
    return []

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    pass

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    return None

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