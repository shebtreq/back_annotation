__author__ = 'Trq'


def main():
    a, b, c, d = 0, 1, 3, "one"
    a, b = b, a
    print(type(c), a, b, c)

    e = (1, 2, 3, 4, 5)
    print(e)

    if a < b:
        print("bla")
    elif a > b:
        print("bla1")
    else:
        print("bla3")

    func(4)


def func(a):
    for i in range(a, 1, -2):
        print(i, end = ' ')
    print()





if __name__ == "__main__": main()





