def count_up(target, n):
    print n
    if n != target:
        count_up(target, n+1)


count_up(5,1)

