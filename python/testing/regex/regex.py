__author__ = 'Trq'

import re



def main():
    a = open('raven.txt')
    for line in a:
        if re.search('(Neverm|Len)ore', line):
            print(line, end='')

    b = open('raven.txt')
    for line in b:
        match = re.search('(Neverm|Len)ore', line)
        if match:
            print(match.group())

    c = open('raven.txt')
    for line in c:
        print(re.sub('(Neverm|Len)ore', '####', line), end = '')

    d = open('raven.txt')
    for line in d:
        match = re.search(' (Neverm|Len)ore', line)
        if match:
            print(line.replace(match.group(), '###'), end='')

    e = open('raven.txt')
    pattern = re.compile('(Neverm|Len)ore', re.IGNORECASE)
    for line in e:
        if re.search(pattern,line):
            re.sub(pattern,'####',line)
            print(line, end='')

    try:
        f = open('ravan.txt')
    except IOError as e:
        print('could not open file:', e)
    else:
             print(line, end = '')

    try:
        f = open('ravan.txt')
        print(line, end = '')
    except IOError as e:
        print('could not open file:', e)




if __name__ == "__main__": main()








