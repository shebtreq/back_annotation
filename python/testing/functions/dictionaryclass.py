__author__ = 'Trq'

class Duck:

    def __init__(self, **kwargs):
        self.dic = kwargs

    def quack(self):
        print('Quackking!!!')

    def getvar(self, k=None):
        if k is not None:
            return self.dic.get(k, None)

    def setvar(self, k=None, v=None):
        if k is not None and v is not None:
            self.dic[k] = v



def main():
    frank = Duck(value=42, colour='white')
    frank.quack()
    print(frank.setvar('colour','blue'))
    print(frank.getvar('colour'))



if __name__ == "__main__": main()
