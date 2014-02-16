def find(l, i):
    # print "this is the list at the top of the chart: ", l
    if len(l) == i+1:
        return l[i]
    else: 
        new_item = l.pop()
        # print "this is what was popped off: ", new_item         
        find(l, i)
        return l[i]

l = ['apple', 'bat', 'cat', 'dog']
print find(l, 1)


"""
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(7) = 13
"""