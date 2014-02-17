# TODO do code review
# TODO Try everything without pop
# Note: doesn't matter where you put the return, as long as after recursive function call(?)

# Multiply all the elements in a list
def multiply_list(l):
    # print 'the length is :', len(l)
    # print "the list at the top of the function is: ", l
    total = 1

    if len(l) == 0:
        return 1
    else:
        last_var = l.pop()
        # print "The term that was popped is: ", last_var
        # print "the new list after popping is: ", l

        total = multiply_list(l) * last_var
        # print 'POST RECURSIVE FUNCTION CALL: Now the length is : ', len(l)
        # print "the term that was popped is: ", last_var
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
    # print "this is the latest list at the top of the function: ", l
# TODO What should the base case be??? see other methods of doing this with other base cases
# TODO Try doing this with switching outer edges
    if l == []: 
        print 100
    else:
        word = l.pop()
        # print "this is the word you just popped ", word
        reverse(l)
        l.insert(0, word)
        # print "this is the list at the bottom of the function after recursive function call: ", l

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

# TODO is there a better way to do this?
# TODO Doesn't seem to matter what I return here 
# TODO: How would you do this so you don't have to modify the list like above? Could you do some sort of counter like I'm trying in the comments below?
# Determines if a string is a palindrome
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
        if some_string[0] == some_string[-1]:
            palindrome(some_string)
            print "this is a palindrome"
            return True
        else:
            print "This is not a palindrome"
            return False

#    return # True or False
"""

# Given the width and height of a sheet of paper, and the number of times to fold it, return the final dimensions of the sheet as a tuple. 
#   Assume that you always fold in half along the longest edge of the sheet.
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

# Count up
# Print all the numbers from 0 to target
def count_up(target, n):
    return