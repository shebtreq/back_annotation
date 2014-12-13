__author__ = 'Trq'


def main():
    testfunc()
    variablefunc(3, 5, 0, 4)
    dictionaryfunc(one=1, two=2, four=4)
    variabledictionaryfunc(3, 5, 0, 4,  one=1, two=2, four=4)


def testfunc(number=1, another=43, onemore=75):
    print('This is a test func',number, another, onemore)


def variablefunc(this, *args):
    print(this, end = ' ')
    for n in args:
        print(n, end=' ')
    print()


def dictionaryfunc(**kwargs):
    print('This is a test function', kwargs['one'], kwargs['two'],kwargs['four'])


def variabledictionaryfunc(this, *args, **kwargs):
    print(this)
    for n in args: print(n)
    for k in kwargs: print(k, kwargs[k])




if __name__ == "__main__": main()