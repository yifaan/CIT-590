import string


def GetName(text):
    f = open(text)
    name = f.readline().lstrip().rstrip()
    while name[0] in string.ascii_uppercase:
        try:
            return name
        except NameError:
            print 'First line should be name with first letter uppercase'


def main():
    print GetName('resume.txt')


if __name__ == '__main__':
    main()
