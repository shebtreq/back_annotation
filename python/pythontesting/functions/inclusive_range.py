__author__ = 'Trq'


def main():
    print('hello')
    for i in inclusive_range(0,25,1):
        print(i, end=' ')

def inclusive_range(*args):
    numargs = len(args)
    if numargs < 1: raise TypeError('requires at least one argument')
    elif numargs == 1:
        start = 0
        stop = args[0]
        step = 1
    elif numargs == 2:
        start = args[0]
        stop = args[1]
        step = 1
    elif numargs == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        raise TypeError('two many arguments supplied')

    i = start
    while i <= stop:
        yield i
        i += step


if __name__ == "__main__": main()