
"""
Exercise 9: Recursion
---------------------

The Evil Wizard Malloc has attacked you and taken away your ability
to use loops!  The only way you can defeat him is by fighting back
using the power of recursion!

Below are function stubs for a variety of functions that are able
to be solved recursively.  For this exercise, you are not allowed
to use:

  * for loops
  * "while" loops
  * You may use list slicing, but you may not use the "reverse" slice
    (e.g, list[::-1])
  * Any built-in function that achieves the same result

You can use the included test_recursion.py script to test that your
functions work (and if you need hints for what the expected input/output 
should be).

"""


# INSTRUCTIONS Multiply all the elements in a list

# NOTE: better to do without pop so it doesn't destroy list. 
#   Don't need all those variables or totals, 
#   Don't need else to reduce indent and lines of code, also will prevent bugs and make eaiser to extend with elif

# Doing With Pop
def multiply_list(l):
    if len(l) == 0:
        return 1
    return l.pop() * multiply_list(l)

# Doing Without Pop
"""
Method 2: 
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return multiply_list(l[0:len(l)-1]) * l[len(l)-1]

Method 3: 
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return multiply_list(l[1:]) * l[0]

Original  less good method: 
def multiply_list(l):
    total = 1

    if len(l) == 0:
        return 1
    else:
        last_var = l.pop()
        total = multiply_list(l) * last_var
    return total
"""



# INSTRUCTIONS Return the factorial of n
def factorial(n):
    if n == 1:
        return 1
    else:
       total = factorial(n-1) * n
    return total



# INSTRUCTIONS Count the number of elements in the list l without using loops or the len() function

# Try without Pop
def count_list(l):

    if l == []: # list_length == 0:
        return 0
    return count_list(l[1:]) + 1

"""
Less good Method: doing with Pop and with unnecessary variables

def count_list(l):
    total = 0
    # print 'total at the top of the function is: ', total
    # print "list at the top is: ", l

    if l == []: # list_length == 0:
        # print total    
        return 0
    else:
        var = l.pop()
        # print "the last item popped is: ", var
        total = count_list(l) + 1
        # print 'total is : ', total
    return total
"""


# INSTRUCTIONS Sum all of the elements in a list without using loops or the sum() function

# NOTE Don't need a variable for pop and don't need total,
#   better to use a slicing function so it does not destroy the original list like pop would. 

def sum_list(l):
    # total = 0
    if l == []: # list_length == 0:
        return 0

    return l[0] + sum_list(l[1:])
    # return l.pop() + sum_list(l)

# TODO revisit why total doesn't matter here
""" # Not as good way: 

 def sum_list(l):
    total = 0

    if l == []: # list_length == 0:
        return 0
    else:
        var = l.pop()
        total = sum_list(l) + var
    return total

"""



# INSTRUCTIONS Reverse a list recursively without loops, the reverse() function or list[::-1]
def reverse(l):

    if len(l) <= 1:
# NOTE better to do <= 1 so that in case someone tries to put in an empty list 
        return l
    return [l.pop()] + reverse(l)


"""
Another method with the switching

def reverse(l):
    if len(l) <= 1:
        return l

    tmp = l[0]
    l[0] = l[-1]
    l[-1] = tmp

    return reverse(l[1:-1])
"""



# INSTRUCTIONS Fibonacci returns the nth fibonacci number. The nth fibonacci number is
#   defined as fib(n) = fib(n-1) + fib(n-2)
def fibonacci(n):
    if n <= 2: #1
        return 1
    else:         
        return fibonacci(n-1) + fibonacci(n-2)



# INSTRUCTIONS Finds the item i in the list l.... RECURSIVELY
# Return the item if it is in the list or None if not found.

def find(l, i):
    # print "this is the list at the top of the chart: ", l
    if len(l) == 0:
        return None
    
    if l[0] == i:
        return l[0]

    return find(l[1:],i)

# NOTE Need to have recall of recursive function in return at all times
#   if the list item is in the list, return conditional, otherwise don't know
#   but can ask the function to RETURN an answer because it knows the answer. 
#   Similar to fold_paper exercise when just sent the answer straight through 
#   without having to recursively calculate anything
#   need to always be conscious returning something when put return recursive function



#  INSTRUCTIONS Determines if a string is a palindrome
# A palindrome is any string that is the same forwards and backwords.
#   (e.g. radar, racecar, aibohphobia)
# Solve recursively, 

def palindrome(some_string):
    if len(some_string) <= 1:
        return True
    
    if some_string[0] == some_string[-1]: 
        return palindrome(some_string[1:-1])
# NOTE This function knows the answer (which is either False from the bottom or True from the base case)
    else:
        return False


# NOTE Normally doesn't matter where you put the return, but it does here because want to keep loop going and not end


"""
# this is only looking at first set of outer letters

def palindrome(some_string):
    if len(some_string) <= 1:
        return []
    else: 
        letter_list = list(some_string)
        first_letter = letter_list.pop(0)
        last_letter = letter_list.pop(-1)
        if first_letter == last_letter:
            some_string = ''.join(letter_list)
            palindrome(some_string)
            return True
        else: 
            return False


"""


# INSTRUCTIONS Given the width and height of a sheet of paper, and the number of times to fold it,
#   return the final dimensions of the sheet as a tuple. 
#   NOTE: Assume that you always fold in half along the longest edge of the sheet.


# NOTE base case return is important to setting tone
#   if have call function at end without any additional operations, will send out final output striaght through
#   will return either what was given in the base case function or the other if/else portion, so just call itself as final return

def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)

    if height >= width:
        height = float(height)/2
    else: 
        width = float(width)/2

    return fold_paper(width, height, folds-1)


"""
# No need to do this because it can just send the result straight through without haven't to calculate anything recursively
def fold_paper(width, height, folds):
    if folds == 0:
        return 
    else:
        if height >= width:
            height = height/2
        else: 
            width = width/2
        fold_paper(width, height, folds-1)

    return (width, height)

"""


# INSTRUCTIONS Count up
# Print all the numbers from 0 to target.
# Use n to keep track of where you're at
# ex, to count from 1 - 100, call count_up(100, 1)
#
# Note: we don't have a test case for this one, so just run this
#       script directly
#
# Note #2: We're printing out the numbers, so this script does not 
#          need to return anything!
def count_up(target, n):
    print n
    if n != target:
        count_up(target, n+1)


# NOTE: count_up doesn't return anything so don't do "print" 
# anytime doing same thing in if and else, in that case, no condition, always running it and pull outside of if stmt
# switch around else to if and get rid of else

"""
    if n == target:
        print n
# NOTE: keeps running even if if stmt met because no return statement to end the function, 
# so the else is necessary
    else:
        print n
        count_up(target, n+1)
"""

if __name__ == "__main__":
    count_up(100, 0)