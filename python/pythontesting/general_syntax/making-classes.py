__author__ = 'Trq'

class Egg:
    def __init__(self, kind = "fried"):
        self.kind = kind

    def whatKind(self):
        return self.kind

def main():
    fried = Egg()
    scrambled = Egg('scrambled')
    print(fried.whatKind())
    print(scrambled.whatKind())
    print(type('blaaa'))
    print(type("bla"))

    num  = 42 / 9
    num1 = 42 // 9
    num2 = round(42/9)
    num3 = int(42.9)
    num4 = float(43)

    n = 42
    s = "This is {} string!".format(n)
    print(s)

    s = '''\
this is a string
line after line
of text and more
text.
    '''
    print(s)

    x = [1, 2, 3]

    x.append(5)
    x.insert(2,7)
    print(type(x),x)

    x = (1, 2, 5)
    print(type(x), x)

    x = 'string'
    print(type(x), x[2:4])


if __name__ == "__main__": main()



















