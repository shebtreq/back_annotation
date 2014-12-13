__author__ = 'Trq'

class Duck:

    def __init__(self, **kwargs):
        self.value = kwargs.get('value', 10)
        self.colour = kwargs.get('colour', 'blue')
        print('A duck has been born!!')

    def quack(self):
        print('Quackking!!!', self.value, self.colour)

    def getcolour(self):
        return self.colour

    def setcolour(self, colour):
        self.colour = colour

    def getvalue(self):
        return self.value

    def setvalue(self, value):
        self.value = value


def main():

    donald = Duck()
    donald.quack()
    print(donald.getvalue())
    print(donald.getcolour())

    frank = Duck(value=42, colour='white')
    frank.quack()
    print(frank.getvalue())
    print(frank.getcolour())



if __name__ == "__main__": main()
