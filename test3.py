def fold_paper(width, height, folds):
    if folds == 0:
        return 
    else:
        if height >= width:
            height = fold_paper(width, height, folds-1)[1]
        else: 
            width = fold_paper(width, height, folds-1)[0]

    return (width, height)

print fold_paper(10,5,3)


"""
TODO - why does this say int object is not subscriptable or has no attribute __getitem__' where it says answer[1]/2 - it should be a tuple?? 
def fold_paper(width, height, folds):
    if folds == 0:
        return 0
    else:
        if height >= width:
            answer = fold_paper(float(width), float(height), folds-1)
            print answer[0]
            # width = answer[1]/2
        else: 
            answer = fold_paper(float(width), float(height), folds-1)
            print answer[0]
            # height = answer[0]/2

    return (width, height)
"""



""" TODO: How would you explain why this doesn't work? Because it works sequentially rather than recursively, 
    meaning don't have to work backwards to be able to then move forward -- it's moving sequentially so when 
    go backwards as recursively functions do, it's spitting back out the first answer

def fold_paper(width, height, folds):
    if folds == 0:
        return 
    else:
        if height >= width:
            height = float(height)/2
            fold_paper(width, height, folds-1)    
        else: 
            width = float(width)/2
            fold_paper(width, height, folds-1)

    return (width, height)
"""



l = ['apple', 'bat', 'cat', 'dog']
l2 = [2,3,4]


"""
fib(1) = 1
fib(2) = 1
fib(3) = 2
fib(4) = 3
fib(5) = 5
fib(6) = 8
fib(7) = 13
"""