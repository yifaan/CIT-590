import csv


def sameAB(ab):
    if ab == '':
        return True
    elif len(ab) % 2 != 0:
        return False
    else:
        if ab[len(ab) / 2] == 'b' and ab[len(ab) / 2 - 1] == 'a':
            return True
        else:
            return False


def binary_search(lst, val):
    midpt = len(lst) / 2
    print lst
    print midpt
    if lst == []:
        return False
    if lst[midpt] == val:
        return True
    else:
        if lst[midpt] > val:
            return binary_search(lst[:midpt], val)

        else:
            return binary_search(lst[midpt + 1:], val)


def flatten(lst):
    print lst
    if lst == []:
        return []
    flattenlst = lst[0] + flatten(lst[1:])
    return flattenlst


def meamer(filename):
    with open(filename, 'r') as csvfile:
        Meamreader = csv.reader(csvfile, delimiter=' ')
        return len([row for row in Meamreader if 'MEAM' in row])


def initials(lst):
    return map(lambda x: x.split()[0][0] + '.' + x.split()[-1][0], lst)


def most_frequent_alphabet(frequency_dictionary):
    return reduce(lambda x, y: x if frequency_dictionary[x] > frequency_dictionary[y] else y, frequency_dictionary)


def main():
    freq = {'a': 3, 'b': 4, 'c': 5, 'd': 2, 'e': 13, 'f': 2}
    print most_frequent_alphabet(freq)


if __name__ == '__main__':
    main()
