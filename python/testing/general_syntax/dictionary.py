__author__ = 'Trq'


def main():
    d = { 'one': 1, 'two': 2, 'thre': 3, 'four': 4, 'five': 5}
    for k in sorted(d.keys()):
        print(k, d[k])

    d = dict(
        one = 1, two = 2, three = 3, four = 4, five = 'five'
    )
    d['seven'] = 7
    for k in sorted(d.keys()):
        print(k, d[k])

    print(d['two'])
    print(d.get('eight','other'))

    s = 'this is a string'
    for i, c in enumerate(s):
        if c == 's' : print('index {} is an s'.format(i))



if __name__ == "__main__": main()
